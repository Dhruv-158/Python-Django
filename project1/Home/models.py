from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField 

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
class services(models.Model):
    service_img = models.CharField(max_length=60)
    service_info = models.CharField(max_length=400)
    # service_dis = models.CharField(max_length=600)

class Cone(models.Model):
    Cone_img=models.CharField(max_length=60)
    Cone_Title = models.CharField(max_length=300)
    Cone_Des = HTMLField()
    