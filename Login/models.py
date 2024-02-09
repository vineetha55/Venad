from django.db import models

# Create your models here.
class tbl_login(models.Model):
    username=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=30,null=True)
    dt=models.DateField(auto_now_add=True,null=True)
    tm=models.TimeField(auto_now_add=True,null=True)