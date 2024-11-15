from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.admin import Group

admin.site.site_header = 'Health-Management-System Administration'
admin.site.site_title = 'Health-Management-System'
admin.site.index_title = 'Health-Management-System Admin'

admin.site.unregister(Group)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username',)
   

admin.site.register(User, CustomUserAdmin)
