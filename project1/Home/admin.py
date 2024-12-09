from django.contrib import admin

from Home.models import Contact,services,Cone

# Register your models here.
admin.site.register(Contact)

class ServiceAdmin(admin.ModelAdmin):
    list_display1=('service_img','service_info')
    
admin.site.register(services,ServiceAdmin)

class coneAdmin(admin.ModelAdmin):
    list_display2=('Cone_img','Cone_title','Cone_description')

admin.site.register(Cone,coneAdmin)    