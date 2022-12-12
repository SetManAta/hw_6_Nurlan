from django.db import models
from datetime import date


class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def get_age(self):
        date.today - self.birth_date

    def __str__(self):
        return self.name

class Employee(AbstractPerson):
    position = models.CharField(max_length=20)
    salary = models.IntegerField(null=True)
    work_experience = models.DateField(null=True)

    def __str__(self):
        return self.position

class Passport(models.Model):
    inn = models.CharField(max_length=16)
    id_card = models.CharField(max_length=10)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE,related_name='passports')

    def get_gender(self):
        if self.inn[0] == 1:
            return 'Women'
        elif self.inn[0] == 2:
            return 'Men'

    def __str__(self):
        return self.inn
    

class WorkProject(models.Model):
    project_name = models.CharField(max_length=20)

    def __str__(self):
        return self.project_name
    

class Membership(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    project = models.ForeignKey(WorkProject,on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return self.date_joined
    

class Client(AbstractPerson):
    adress = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.adress
    

class VIPClient(Client):
    vip_status_start = models.DateField(null=True)
    donation_amount = models.IntegerField(null=True)

    def __str__(self):
        return self.vip_status_start
    
    