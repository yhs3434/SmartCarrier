from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GpsSerializer
from .models import Gps

# Create your views here.

class GpsViewSet(viewsets.ModelViewSet):
    queryset = Gps.objects.all()
    serializer_class = GpsSerializer