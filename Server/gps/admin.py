from django.contrib import admin
from .models import Gps

# Register your models here.

@admin.register(Gps)
class GpsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'latitude', 'longitude', 'upload_date']
    list_display_links = ['id']