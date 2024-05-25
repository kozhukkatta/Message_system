from sqlite3 import Date
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

# Create your models here.
class Login(models.Model):
    username = models.CharField(primary_key=True,max_length=10, blank=True)
    password=models.CharField(max_length=10, blank=True)
    fullname = models.CharField(max_length=20, blank=True)
    dob = models.DateField(max_length=20, blank=True)
    role = models.CharField(max_length=20,default='user',blank=True)
    email = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=6, blank=True)
    address = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    status=models.IntegerField(default=1,blank=True)
    #image = models.ImageField(upload_to="media/profile", blank=True)
    class Meta:
        db_table="login"

class Message(models.Model):
    mid = models.CharField(primary_key=True,max_length=10, blank=True)
    username = models.CharField(max_length=10, blank=True)
    option = models.CharField(max_length=10, blank=True)
    suname= models.CharField(max_length=10, blank=True,default='null')
    msg = models.CharField(max_length=5000, blank=True)
    date = models.DateField()
    status=models.IntegerField(default=1,blank=True)
    class Meta:
        db_table="message"
    #def __str__(self):
      #  return str(self.user)