from django.conf.urls import url
from django.urls import path
from gps import views

urlpatterns = [
    path('', views.gps_list),
    path('<int:pk>/', views.gps_detail),
]