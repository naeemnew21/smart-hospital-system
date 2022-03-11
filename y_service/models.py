from django.db import models
from user.models import MyUser
from datetime import timedelta, date, datetime


SERVICES = [
    ('appointment', 'appointment'),
    ('pharmacy', 'pharmacy'),
    ('bloodbank', 'bloodbank'),
    ('laboratory', 'laboratory'),
    ('x-ray', 'x-ray'),
    ('ambulance', 'ambulance'),
]

CANCELED = [
    ('patient', 'patient'),
    ('staff', 'staff'),
]

class Service(models.Model):
    """
        - start service
        - define service   : as a model --> models.Foreignkey(CustomModel) or keep None if No model
        - name of service  : required particular in case of no model
        - request_owner    : user who requests the service
        - request_traget   : user who benefits from the result 
                             - in case of appointment   : doctor  get benefit from  patient (money)
                             - in case of other service : patient get benefit from the final result
                                                         - medecines if pharmacy
                                                         - blood if blood bank
                                                         - report if laboratory
                                                         - x-ray if x-ray
        - staff_user       : user who do the job (service)
                             - appointment : secretary
                             - pharmacy    : parmacist
                             
        - request          : request from patient in all cases to staff_user  ### needs reconsider
                             - appointment    : from patient to secretary
                             - other services : from patient to service_staff_user
                             
        - response_details : after patient requst service, service_staff_user replies with:
                                1- skip this step : No reply jump to next step if no need
                                            - like in appointment you already know schedule and price
                                2- text : shows some notes like price.
                                3- form : has check fields like payment confirm.
                                
        - confirm          : patient is the user who can confirm
                            - in case of service that doesn't have response it turned to True
                              in the same time of (request)
        
        - result           : reuest --> response --> confirm --> result
                            - appointment : take an appointment
                            - pharmacy    : take medecines
                            - laboratory  : receive report
                            - x-ray       : receive x-ray
                            
        = in case of problems (rejection - cancellation - disable)

        - rejected         : instead of reply to request with response staff_user reply with rejection
        - reject_reasons   : reasons of rejection
        
        - canceled         : cancel probabilities
                            - after make request : patient wants to cancel request
                            - after confirm      : patient or staff_user wants to cancel request
        
        - cancel_reasons   : this field important to return money if you payed 
        - cancelled_by     : patient or staff_user  

        - disabled         : if today date exceeds expire_date of service of disabled by superuser
        - expire_date      : = (create_date + expire_days) after that become disabled
        
        ====================================================
        = required fields                 : - name
                                            - model
        = required but has default values : - request_owner
                                            - request_traget
                                            - staff_user
        = optional    : - response_details
                        - result
                        - reject_reasons
                        - cancel_reasons
                     
        = auto assign : - create_date
                        - expire_date
        =========================================================
            +++++++ Full Algorithm +++++++
            
                  |--->> reject --->> return to request
        request --|-->> cancel  --->> return to request (for patient only)
                  |--->> response  |----->> cnacel --->> return to request (for patient and staff)
                                   |
                                   |--->> confirm |--->> cancel --->> return to request (for staff and <patient>)
                                                  |
                                                  |--->> result --->> dischare --->> end
       if no decesion taken until expire_date it becomes disabled
       ===============================================================
       
    """
    
    """refer to model of requested service
        - this model must have patient and doctor
    """
    model            = None 
    
    """refers to the name of service"""
    #service_name     = models.CharField(choices=SERVICES, max_length=20) # required
    

    patient          = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='service_patient')
    doctor           = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='service_doctor')
    
    """in case of appointment: secretary or receptionist"""
    staff_user       = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='service_staff')
    
    create_date      = models.DateField(auto_now_add=True)
    
    """request from patient to staff of service"""
    request          = models.BooleanField(default = False) 
    request_date     = models.DateField(blank=True, null=True)
    
    response_details = None # may be text field or model
    response_date    = models.DateField(blank=True, null=True)
    
    """that means you may probably have to pay money"""
    confirm          = models.BooleanField(default = False)  #--------->>>> start new request if False
    confirm_date     = models.DateField(blank=True, null=True)
    
    result           = None # may be text field or model      #-------------->>>> end
    result_date      = models.DateField(blank=True, null=True)
    
    """to confirm that the patient has received results and payed money"""
    discharge        = models.BooleanField(default = False)
    discharge_date   = models.DateField(blank=True, null=True)
    
    # in case of problems (rejection - cancellation - disable)
    
    reject        = models.BooleanField(default = False)
    reject_reasons   = None # may be text field or model
    reject_date      = models.DateField(blank=True, null=True)

    
    """this field important in case of you payed money"""
    
    canceled         = models.BooleanField(default = False)
    cancel_reasons   = None # may be text field or model
    cancelled_by     = models.CharField(choices=CANCELED, max_length=7, blank=True, null=True)
    cancel_date      = models.DateField(blank=True, null=True)
    
    """if current date exceeds the start_date of service with for example month"""
    disabled         = models.BooleanField(default = False)   #-------------------->>>> end
    disabled_date    = models.DateField(blank=True, null=True)
    expire_days      = models.PositiveIntegerField(default = 7)
    expire_date      = models.DateField(blank=True, null=True) # edited in save
    
    
    
    class Meta:
        abstract = True
        
        
    def __str__(self):
        return self.model.__str__()
        
    def save(self, *args, **kwargs):
        if self.create_date == None:
            self.expire_date = date.today() + timedelta(self.expire_days)
        else:
            self.expire_date = self.create_date + timedelta(self.expire_days)
        
        if self.model != None:
            self.patient = self.model.patient
            self.doctor  = self.model.doctor
            
        super().save(*args, **kwargs)
       
       

class ServiceRequest(Service):
    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        if self.expire_date != None:
            self.check_expire()
        super().save(*args, **kwargs)
        
        
        
    def get_status(self):
        if self.result != None:
            return "result"
        elif self.confirm:
            return "confirm"
        elif self.response_details != None:
            return "response"
        elif self.request:
            return "request"
        else :
            return "start"
        
    def get_next_step(self):
        status = self.get_status()
        if status == "start":
            return "request"
        elif status == "request":
            return "response"
        elif status == "response":
            return "confirm"
        elif status == "confirm":
            return "result"
        elif status == "result":
            return None
        
        
    def cancel_request(self):
        self.confirm          = False
        self.response_details = None
        self.request          = False 
        self.cancel_date      = date.today()
            
            
    def reject_request(self):
        self.request     = False 
        self.reject_date = date.today()
    
    
    def disable_request(self):
        self.disabled      = True
        self.disabled_date = date.today()
 
 
    def discharge_request(self):
        self.discharge      = True
        self.discharge_date = date.today()
               
               
    def check_expire(self):
        expire = datetime.strptime(str(self.expire_date), "%Y-%m-%d").date()
        if expire < date.today():
            self.disable_request()
    

    
    