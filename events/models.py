from django.db.models import (
    CharField,
    DateTimeField,
    PositiveIntegerField,
    ManyToManyField,
    ForeignKey, PROTECT
)

from shared.models import BaseModel
from users.models import User


class Event(BaseModel):
    name = CharField(max_length=80)
    description = CharField(
        max_length=1000,
    )
    start_datetime = DateTimeField()
    end_datetime = DateTimeField(null=True)
    max_attendants = PositiveIntegerField()
    location = CharField(max_length=200)  # could be address relation

    attendants = ManyToManyField(User, related_name='attended_events', blank=True) 
    organizer = ForeignKey(User, on_delete=PROTECT, related_name='organized_events')

    class Meta:
        db_table = "events"
