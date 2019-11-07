from django.db import models

# Create your models here.


class Employee(models.Model):
    ename = models.CharField(max_length=50)
    eaddress = models.CharField(max_length=50)
    esalary = models.FloatField()
    ecompany = models.CharField(max_length=50)
    eage = models.IntegerField()


