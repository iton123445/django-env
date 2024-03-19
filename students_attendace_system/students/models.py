from django.db import models

class Students(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    course = models.CharField(max_length=255)
    contactnumber = models.IntegerField(null=True)