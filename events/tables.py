import django_tables2 as tables
from .models import Event
class EventsTable(tables.Table):
    class Meta:
        model = Event
