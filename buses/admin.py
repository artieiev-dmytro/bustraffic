from django.contrib import admin

from .models import Bus

class BusAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_city', 'to_city', 'bus_time')
    search_fields = ('name',)


admin.site.register(Bus, BusAdmin)
