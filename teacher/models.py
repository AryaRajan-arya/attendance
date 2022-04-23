from django.db import models
class student(models.Model):
    name= models.CharField(max_length=255,null=True)
    phone= models.CharField(max_length=255,null=True)
    Rollno= models.CharField(max_length=255,null=True)
    locationNo=models.CharField(max_length=255,null=True)
    date=models.DateTimeField(auto_now_add=True)
    
# Create your models here.
