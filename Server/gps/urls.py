from django.urls import path
from gps import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.gps_list),
    path('<int:pk>/', views.gps_detail),
    path('my/', views.MyRecentGpsPosition.as_view()),
    path('beacon/', views.BeaconList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)