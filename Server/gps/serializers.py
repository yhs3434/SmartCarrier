from .models import Gps, Beacon
from rest_framework import serializers

class GpsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gps
        fields = ('pk', 'name', 'latitude', 'longitude', 'upload_date')

class BeaconSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beacon
        fields = ('pk', 'beacon', 'distance')