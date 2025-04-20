from django.db.models import (
    CharField,
    DateTimeField,
    PositiveIntegerField,
    ManyToManyField,
    ForeignKey, PROTECT, CASCADE
)

from shared.models import BaseModel
from users.models import User


class Location(BaseModel):
    street_name = CharField(max_length=200)
    street_number = CharField(max_length=10)
    neighborhood = CharField(max_length=100)
    city = CharField(max_length=100)
    state = CharField(max_length=100)
    country = CharField(max_length=100)
    postal_code = CharField(max_length=20)

    class Meta:
        db_table = "locations"

class Event(BaseModel):
    name = CharField(max_length=80)
    description = CharField(
        max_length=1000,
    )
    start_datetime = DateTimeField()
    end_datetime = DateTimeField(null=True)
    max_attendants = PositiveIntegerField()
    location = ForeignKey(Location, on_delete=CASCADE)

    organizer = ForeignKey(User, on_delete=PROTECT, related_name='organized_events')

    class Meta:
        db_table = "events"
