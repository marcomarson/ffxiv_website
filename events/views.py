from django.shortcuts import render
from .models import Event
import calendar
import django_tables2 as tables
from .tables import EventsTable



def event_list(request):
    queryset = Event.objects.all()
    table = EventsTable(Event.objects.all())

    context = {
        'events': queryset,
        'calendar': table,


    }
    print(context['calendar'])
    return render(request, 'event.html', context)
