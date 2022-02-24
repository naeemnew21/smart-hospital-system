
import re
import time
import datetime

city_code = {
    '01' : ['Cairo' , 'القاهرة'],
    '02' : ['Alexandria', 'الإسكندرية'],
    '03' : ['Port Said', 'بورسعيد'],
    '04' : ['Suez', 'السويس'],
    '11' : ['Damietta', 'دمياط'],
    '12' : ['Dakahlia', 'الدقهلية'],
    '13' : ['Sharqia', 'الشرقية'],
    '14' : ['Qalyubia', 'القليوبية'],
    '15' : ['Kafr al sheikh', 'كفر الشيخ'],
    '16' : ['Gharbia', 'الغربية'],
    '17' : ['Menoufia', 'المنوفية'],
    '18' : ['Behira', 'البحيرة'],
    '19' : ['Ismailia', 'الإسماعيلية'],
    '21' : ['Giza', 'الجيزة'],
    '22' : ['Beni suef', 'بني سويف'],
    '23' : ['Fayoum', 'الفيوم'],
    '24' : ['Al minya', 'المنيا'],
    '25' : ['Assiut', 'أسيوط'],
    '26' : ['Sohag', 'سوهاج'],
    '27' : ['Qna', 'قنا'],
    '28' : ['Aswan', 'أسوان'],
    '29' : ['Luxor', 'الأقصر'],
    '31' : ['Red sea', 'البحر الأحمر'],
    '32' : ['New valley', 'الوادى الجديد'],
    '33' : ['Matrouh', 'مطروح'],
    '34' : ['North sinai', 'شمال سيناء'],
    '35' : ['South sinai', 'جنوب سيناء'],
    '88' : ['Outside The Republic', 'خارج الجمهورية'],
    }

class ID_Valid:
    def __init__(self, ID): 
        self.id = ID
        self.date_limit = [i for i in time.localtime()[:3]] # (year, month, day)

    def is_valid(self):
        x = self.check_re()
        y = self.check_max_date()
        z = self.check_month_day()
        k = self.check_code()
        return x and y and z and k  # -> True or False

    def get_birth(self):
        if self.is_valid() :
            year  = int(self.id[1:3]) # two digits
            month = int(self.id[3:5])
            day   = int(self.id[5:7])
            if self.id[0] == '2':
                year += 1900
            else :
                year += 2000
            return "{}-{}-{}".format(year, month, day)

    def get_city(self):
        if self.is_valid() :
            return city_code[self.id[7:9]]

    def get_sex(self):
        if self.is_valid() :
            if int(self.id[12]) % 2 == 0:
                return 'Female'
            return 'Male'

    def __str__(self):
        return self.id

    def __iter__(self):
        for i in self.id :
            yield i

    def check_re(self):
        x = re.findall('[23]\d{11}[1-9]{2}', self.id)
        if len(x) == 1:
            return True
        return False
    
    def check_max_date(self):
        if not(self.check_re()):
            return False
        year  = int(self.id[1:3]) # two digits
        month = int(self.id[3:5])
        day   = int(self.id[5:7])
        
        if self.id[0] == '3':
            year += 2000
            if (year < self.date_limit[0] ):
                return True
            if (year == self.date_limit[0] ):
                if (month < self.date_limit[1] ):
                    return True
                if (month == self.date_limit[1] ):
                    if (day <= self.date_limit[2] ):
                        return True     
        else :
            return True
        return False

    def check_month_day(self):
        if not(self.check_re()):
            return False
        year  = int(self.id[1:3])
        month = int(self.id[3:5])
        day   = int(self.id[5:7])
        if self.id[0] == '2' :
            year += 1900
        else :
            year += 2000
        try :
            datetime.datetime(year = year, month = month, day=day)
            return True
        except ValueError:
            return False

    def check_code(self):
        if not(self.check_re()):
            return False
        if self.id[7:9] in city_code :
            return True
        return False
    
    
