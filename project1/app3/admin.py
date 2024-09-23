from django.contrib import admin
from .models import authenticate
 
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)  # Display the username in the admin list view
 
admin.site.register(authenticate, UserAdmin)
