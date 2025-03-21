from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('zapis', views.zapis, name='zapis'),
    path('calendar', views.calendar_view, name='calendar'),
    path('calendar/jdut-podtvergdeniy', views.calendar_gdut_view, name='calendar-gdut'),
    path('calendar/custom', views.CustomCal, name='custom'),
    path('zapis-usluga', views.zapis_usluga, name='zapis-usluga'),
    path('calendar/zapis-edit', views.calendar_edit, name='calendar-gdut'),
    path('politica-conf', views.politica_conf, name='politica-conf'),
    path('client-card', views.client_card, name='client-card'),
    path('usluga', views.usluga, name='usluga'),
    path("api/chiara-chat/", views.chiara_chat, name="chiara_chat"),

]