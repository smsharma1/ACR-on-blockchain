from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from django.contrib.admin.widgets import AdminDateWidget

class CustomUser(AbstractUser):
    # add additional fields in here
    # ID = models.AutoField(primary_key=True)
    #ID is default added by django named as id
    USER_TYPE_CHOICES =(
        (1,'ratee'),
        (2,'IO'),
        (3,'RO'),
        (4,'SRO'),
        (5,'AO'),
        (6,'Admin'),
        (7,'Clerk'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default=0)
    firstname = models.CharField(default="Shubham",max_length=50)
    lastname = models.CharField(default="Sharma",max_length=50)
    # is_student = models.BooleanField('student status',default=False)

    def __str__(self):
        return self.email

class Appraisal(models.Model):
    AppID = models.AutoField(primary_key=True,default=1)
    RateeID = models.IntegerField(default=1)
    IOID = models.IntegerField(default=2)
    ROID = models.IntegerField(default=3)
    SROID = models.IntegerField(default=4)
    AOID = models.IntegerField(default=5)
    ClerkID = models.IntegerField(default=7)

class LeaveRecord(models.Model):
    OfficerID = models.IntegerField(default=1)
    From = models.DateField(default=date.today)
    To = models.DateField(default=date.today)