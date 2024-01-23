from django.db import models


class signup(models.Model):
    objects = None
    username = models.CharField(max_length=50)
    password =  models.CharField(max_length=50)
    email=models.EmailField()

class register(models.Model):
    objects = None
    first=models.CharField(max_length=50)
    last=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    pincode=models.IntegerField()
    course=models.CharField(max_length=50)
    email=models.EmailField()
