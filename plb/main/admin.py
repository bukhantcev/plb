from django.contrib import admin
from .models import Uslugi_groups, Uslugi, Sertifikate, Klients, Zapis


admin.site.register(Uslugi)
admin.site.register(Uslugi_groups)

@admin.register(Sertifikate)
class EventAdmin(admin.ModelAdmin):
    list_display = ( 'file', 'name', 'priority',)
    list_editable = ('name', 'priority',)


@admin.register(Klients)
class EventAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'phone',)
    list_editable = ('phone',)


@admin.register(Zapis)
class EventAdmin(admin.ModelAdmin):
    list_display = ( 'create_date', 'client_name', 'phone', 'procedura_name', 'date_proceduri', 'time_proceduri', 'zapis_status', 'price',)
    list_editable = ('client_name', 'procedura_name', 'date_proceduri', 'time_proceduri', 'zapis_status', 'price',)


