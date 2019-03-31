from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
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
    # is_student = models.BooleanField('student status',default=False)

    def __str__(self):
        return self.email