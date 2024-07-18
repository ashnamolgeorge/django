from django.db import models

# Create your models here.
class Doctors(models.Model):
    category=models.CharField(max_length=50)
    doctors_name=models.CharField(max_length=60)
    doctor_image=models.ImageField()
    experiance=models.IntegerField(default=2)
    contact=models.IntegerField(default=1)
    
    
    
