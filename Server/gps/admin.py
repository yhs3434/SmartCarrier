from django.contrib import admin
from .models import Gps, Beacon

# Register your models here.

@admin.register(Gps)
class GpsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'latitude', 'longitude', 'upload_date']
    list_display_links = ['id']

@admin.register(Beacon)
class BeaconAdmin(admin.ModelAdmin):
    list_display = ['id', 'beacon', 'distance']
    list_display_links = ['id']