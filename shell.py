from postq.models import *

person1 = Passport(employee=Employee.objects.create(name='Nurlan',birth_date='1990-01-01',position='Dir', salary=100000, work_experience='2020-02-02'),inn='1234567890123456',id_card='1234567890')
person1.save()

