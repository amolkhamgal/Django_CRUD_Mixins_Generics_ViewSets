from django.db import models

# Create your models here.

class Employee(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=40)
    gender=models.CharField(max_length=20)
    age=models.IntegerField()
    salary=models.IntegerField()
