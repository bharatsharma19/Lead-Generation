from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    eid = models.IntegerField()
    esalary = models.IntegerField()
    egender = models.CharField(max_length=1)
    estatus = models.CharField(max_length=30)
    edept = models.CharField(max_length=30)
    egrade = models.IntegerField()
    e_personalId = models.CharField(max_length=30)
    e_post = models.CharField(max_length=30)
