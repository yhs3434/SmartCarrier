from .models import Gps
from rest_framework import serializers

class GpsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gps
        fields = ('name', 'latitude', 'longitude', 'upload_date')