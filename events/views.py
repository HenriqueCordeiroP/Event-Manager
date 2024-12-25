from rest_framework import viewsets

from events.models import Event
from events.serializers import EventSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('start_datetime')
    serializer_class = EventSerializer