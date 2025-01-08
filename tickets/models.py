from django.db.models import ForeignKey, PROTECT, CharField, IntegerChoices, SmallIntegerField

from shared.models import BaseModel
from users.models import User
from events.models import Event
from commerce.models import Order, Price
from shared.utils import generate_alphanumerical_token
from shared.constants import TICKET_CODE_LENGTH


class Ticket(BaseModel):
    class Status(IntegerChoices):
        PENDING = 1
        CANCELLED = 2
        CONFIRMED = 3

    user = ForeignKey(User, on_delete=PROTECT)
    event = ForeignKey(Event, on_delete=PROTECT)
    order = ForeignKey(Order, on_delete=PROTECT)
    price = ForeignKey(Price, on_delete=PROTECT)

    code = CharField(max_length=TICKET_CODE_LENGTH, blank=True, unique=True)

    status = SmallIntegerField(default=Status.PENDING)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_alphanumerical_token(TICKET_CODE_LENGTH)
        super().save(*args, **kwargs)

    class Meta:
        db_table = "tickets"
