from django.contrib import admin
from .models import Mission

class MissionAdmin(admin.ModelAdmin):
    """
        this class is MissionAdmin class and set fields of admin page of
        Mission model.
    """
    model = Mission
    list_display = ('name', 'courier', 'is_get', 'start_time', 'done', 'done_time', 'origin_latitude', 'origin_longitude', 'destination_latitude', 'destination_longitude')
    list_filter = ('courier', 'name', 'is_get', 'done')
    search_fields = ('courier', )
    ordering = ('start_time', 'done_time')
    readonly_fields = ['start_time', 'done_time']
    fieldsets = (
        ('Details', {
            "fields": (
                'name',
                'courier',
                'origin_latitude',
                'origin_longitude', 
                'destination_latitude', 
                'destination_longitude',
            ),
        }),
        
        ('Important Dates', {
            "fields": (
                'start_time',
                'done_time',
            ),
        }),
        ('Status', {
            "fields": (
                'is_get',
                'done',
            ),
        }),
        
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("name", "courier", "origin_latitude", "origin_longitude", "destination_latitude", "destination_longitude")
        }),
    )

admin.site.register(Mission, MissionAdmin)