from django.db import models

# Create your models here.
class Employee(models.Model):
    title =  models.CharField(max_length=10)
    fname = models.CharField(max_length=100)
    lname =  models.CharField(max_length=100)
    gender =  models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    dob =  models.DateField(auto_now=False)
    position =  models.CharField(max_length=100)
    address =  models.CharField(max_length=200)
    zipcode =  models.CharField(max_length=100)
    district =  models.CharField(max_length=100)
    phone =  models.CharField(max_length=100)
    email =   models.CharField(max_length=100)
    resume =  models.ImageField(upload_to='pics')
