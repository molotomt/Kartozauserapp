from msilib.schema import Class
from pyexpat import model
from tabnanny import verbose
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Userdetails, Userprofile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class userdetailsadmin(admin.StackedInline):
    model = Userdetails
    can_delete = False
    verbose_name_plural = 'Userdetails'

class CustomizedUserdetails(UserAdmin):
    inlines = (userdetailsadmin, )

admin.site.unregister(User)    
admin.site.register(User, CustomizedUserdetails )
admin.site.register(Userprofile)


@admin.register(Userdetails)
class UserAdmin(OSMGeoAdmin):
    list_display = ('home_address', 'location')
