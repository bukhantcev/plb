from django.contrib import admin
from .models import Uslugi_groups, Uslugi, Sertifikate


admin.site.register(Uslugi)
admin.site.register(Uslugi_groups)

@admin.register(Sertifikate)
class EventAdmin(admin.ModelAdmin):
    list_display = ( 'file', 'name', 'priority',)
    liink_display = ('file',)
    list_editable = ('name', 'priority',)

