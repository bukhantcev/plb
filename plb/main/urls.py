from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('zapis', views.zapis, name='zapis'),
    path('calendar', views.calendar_view, name='calendar'),
    path('calendar/jdut-podtvergdeniy', views.calendar_gdut_view, name='calendar-gdut'),
    path('calendar/custom', views.CustomCal, name='custom'),
]