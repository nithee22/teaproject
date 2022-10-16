from django.contrib import admin
from .models import tea 




class teaAdmin(admin.ModelAdmin):
    list_display=('name','price','quantity')

admin.site.register(tea , teaAdmin)