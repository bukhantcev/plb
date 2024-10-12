from django.contrib import admin
from .models import Uslugi_groups, Uslugi, Sertifikate, Klients, Zapis


admin.site.register(Uslugi)
admin.site.register(Uslugi_groups)

@admin.register(Sertifikate)
class SertifikateAdmin(admin.ModelAdmin):
    list_display = ( 'file', 'name', 'priority',)
    list_editable = ('name', 'priority',)


@admin.register(Klients)
class KlientsAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'phone',)
    list_editable = ('phone',)


@admin.register(Zapis)
class ZapisAdmin(admin.ModelAdmin):
    list_display = ( 'create_date', 'client_name', 'phone', 'procedura_name', 'date_proceduri', 'time_proceduri', 'zapis_status', 'price',)
    list_editable = ('client_name', 'procedura_name', 'date_proceduri', 'time_proceduri', 'zapis_status', 'price',)
    list_filter = ('client_name', 'phone', 'procedura_name', 'date_proceduri', 'time_proceduri', 'zapis_status',)


