from django.db.models import (
    CharField,
    DateTimeField,
    PositiveIntegerField,
    ManyToManyField,
    ForeignKey, PROTECT
)

from shared.models import BaseModel
from users.models import User
from events.models import Event

class Ticket(BaseModel):
    owner = ForeignKey(User, on_delete=PROTECT)
    previous_owner = ForeignKey(User, on_delete=PROTECT, null=True)
    event = ForeignKey(Event, on_delete=PROTECT)
    
    class Meta:
        db_table = "events"
