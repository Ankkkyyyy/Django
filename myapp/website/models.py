from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# parent class isliye daalrhe ki parent kepass jitne feature hai vosbh aajaye
# yahape..
class Student(models.Model):
    name = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    age=models.IntegerField(max_length=10)
    is_active=models.BooleanField(default=False)


