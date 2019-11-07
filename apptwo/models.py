from django.db import models

# Create your models here.


class Student(models.Model):
    sname = models.CharField(max_length=50)
    saddress = models.CharField(max_length=50)
    sfees = models.FloatField()
    scollege = models.CharField(max_length=50)
    sage = models.IntegerField()
