from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from drf_spectacular.utils import extend_schema

from events.models import Event
from events.serializers import EventSerializer
from events.permissions import IsEventCreator

@extend_schema(tags=["Events"])
class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("start_datetime")
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsEventCreator]

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsEventCreator()]
        return super().get_permissions()
