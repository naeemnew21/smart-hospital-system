from rest_framework import serializers
from .models import Medicine, Prescription, RequestPrescription







class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['medicine_name', 'number_of_units', 'unit', 'number_of_times', 'time', 'notes']
        
    def to_representation(self, instance):
        data                     = super().to_representation(instance)
        context                  = {}
        context['id']            = instance.id
        
        data.update(context)
        return data
        
        
        
        
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['patient', 'doctor', 'date', 'medicines']
        
    def to_representation(self, instance):
        data                       = super().to_representation(instance)
        context                    = {}
        context['doctor_name']     = instance.doctor.first_name
        context['prescription_id'] = instance.id
        context['details']         = {}
        for i in instance.medicines.all():
            context['details'][i.id] = {
                'medicine_name'   :i.medicine_name,
                'number_of_units' :i.number_of_units,
                'unit'            :i.unit,
                'number_of_times' :i.number_of_times,
                'time'            :i.time,
                'notes'           :i.notes
            }
        
        data.update(context)
        return data
        

