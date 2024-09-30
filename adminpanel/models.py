from django.db import models


# Create your models here.
class regdata(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    C_password=models.CharField(max_length=100)

class coursedata(models.Model):
    Course=models.CharField(max_length=100)

class roledata(models.Model):
    Role=models.CharField(max_length=100)

class referencedata(models.Model):
    Reference=models.CharField(max_length=200)
