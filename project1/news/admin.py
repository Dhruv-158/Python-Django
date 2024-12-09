from django.contrib import admin
from news.models import News
# Register your models here.

class Newadmin(admin.ModelAdmin):
    list_display = ('news_img','news_title','news_desc')
    
admin.site.register(News,Newadmin)