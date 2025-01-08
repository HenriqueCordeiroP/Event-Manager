from django.db.models import ForeignKey, PROTECT, CharField

from shared.models import BaseModel
from users.models import User
from events.models import Event
from commerce.models import Order, Price
from shared.utils import generate_alphanumerical_token
from shared.constants import TICKET_CODE_LENGTH

class Ticket(BaseModel):
    user = ForeignKey(User, on_delete=PROTECT)
    event = ForeignKey(Event, on_delete=PROTECT)
    order = ForeignKey(Order, on_delete=PROTECT)
    price = ForeignKey(Price, on_delete=PROTECT)

    code =  CharField(max_length=TICKET_CODE_LENGTH, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.code:  
            self.code = self.generate_alphanumerical_token(TICKET_CODE_LENGTH)
        super().save(*args, **kwargs)

    class Meta:
        db_table = "tickets"
    