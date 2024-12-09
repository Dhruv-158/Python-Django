from django.db import models 
from tinymce.models import HTMLField 

class News(models.Model):
    news_img = models.CharField(max_length = 100)
    news_title = models.CharField(max_length=100)
    news_desc = HTMLField() 
    
    def __str__(self):
        return self.news_title
# Create your models here.
 