from django.db import models

# Create your models here.

class UserReg(models.Model):
    name=models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    email = models.EmailField()
    locality = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
