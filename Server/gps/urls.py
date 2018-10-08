from django.urls import path
from gps import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.gps_list),
    path('<int:pk>/', views.gps_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)