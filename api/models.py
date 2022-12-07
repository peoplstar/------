from django.db import models

# Create your models here.

class Login(models.Model):
    lms_id = models.CharField(max_length = 15, primary_key = True)
    lms_pw = models.CharField(max_length = 30)
    
    
class Status(models.Model):
    day = models.CharField(max_length = 15, primary_key = True)
    place = models.CharField(max_length = 20)

       
class Reservation(models.Model):
    lms_id = models.CharField(max_length = 15, primary_key = True)
    day = models.CharField(max_length = 10)
    place = models.CharField(max_length = 20)
    start_time = models.CharField(max_length = 10)
    end_time = models.CharField(max_length = 10)
    appd = models.BooleanField(default = False)

class BoardStatus(models.Model):
    idx = models.IntegerField(max_length = 10, primary_key = True)
    title = models.CharField(max_length = 25)
    day = models.CharField(max_length = 15)
    
class BoardWrite(models.Model):
    idx = models.CharField(max_length = 10, primary_key = True)
    title = models.CharField(max_length = 25)
    day = models.CharField(max_length = 15)
    contents = models.CharField(max_length = 500)
    
    