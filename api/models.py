from django.db import models

# Create your models here.

class Login(models.Model):
    lms_id = models.CharField(max_length = 15, primary_key = True)
    lms_pw = models.CharField(max_length = 30)
    
    
class Status(models.Model):
    day = models.CharField(max_length = 15, primary_key = True)
    place = models.CharField(max_length = 20)

class Reservation(models.Model):
    mode = models.CharField(max_length = 5)
    lms_id = models.CharField(max_length = 15, primary_key = True)
    day = models.CharField(max_length = 10)
    place = models.CharField(max_length = 20)
    start_time = models.CharField(max_length = 10)
    end_time = models.CharField(max_length = 10)
    appd = models.CharField(max_length = 1)

class Comments(models.Model):
    mode = models.CharField(max_length = 5)
    lms_id = models.CharField(max_length = 15, primary_key = True)
    title = models.CharField(max_length = 25)    
    comment = models.CharField(max_length = 50)    

class BoardStatus(models.Model):
    lms_id = models.CharField(max_length = 15, primary_key = True)
    
class BoardWrite(models.Model):
    lms_id = models.CharField(max_length = 15, primary_key = True)
    title = models.CharField(max_length = 25)
    day = models.CharField(max_length = 15)
    contents = models.CharField(max_length = 500)

class BoardRead(models.Model):
    title = models.CharField(max_length = 25)
    
    