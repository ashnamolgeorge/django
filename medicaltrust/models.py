from django.db import models
from adminhandle.models import*

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    contact=models.IntegerField(default=0)


class Contacts(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    subject=models.CharField(max_length=50)
    your_message=models.CharField(max_length=200)

class Dlist(models.Model):
    doctor_name=models.CharField(max_length=50) 
    department=models.CharField(max_length=60)
    qualification=models.CharField(max_length=50)



class myac(models.Model):
    user_id=models.ForeignKey(Registration,on_delete=models.CASCADE) 
    doctor_id=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    date=models.CharField(max_length=20) 
    time=models.TimeField()
    status=models.IntegerField(default=0)
    



        