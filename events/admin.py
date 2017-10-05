from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display= ["title", "maxplayers", "content" ]

    class Meta:
        model = Event

admin.site.register(Event, EventAdmin)

# Register your models here.
