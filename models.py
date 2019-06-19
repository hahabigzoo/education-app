#-*- encoding=utf-8 -*-

from django.db import models
from django.template.defaultfilters import default
from django.db.models.fields import PositiveSmallIntegerField

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    privilege = models.PositiveSmallIntegerField()
    audited = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.username


class Parents(models.Model):
    username = models.ForeignKey('Users', primary_key=True, on_delete=models.CASCADE)  
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    name = models.CharField(max_length=4)
    balance = models.PositiveIntegerField(default=0)
    child_name = models.CharField(max_length=10)
    child_age = models.IntegerField(default=10)
    child_sex = models.CharField(max_length=6)
    
    def __unicode__(self):
        return self.username
    
    
class Lessons(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    
    def __unicode__(self):
        return self.username.id
    
    
class Comments(models.Model):
    username = models.ForeignKey('Users', on_delete=models.CASCADE)
    starts = models.PositiveSmallIntegerField(default=5)
    words = models.CharField(max_length=50)
    images = models.ImageField(upload_to='img')