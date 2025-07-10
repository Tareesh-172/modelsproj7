from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    reg_name=models.CharField(max_length=20)
    reg_age=models.IntegerField()
    reg_loc=models.CharField(max_length=20)
    reg_marks=models.IntegerField()
    reg_date=models.DateField(max_length=20)
    reg_user=models.CharField(max_length=10)