from django.db.models import (
    PROTECT,
    ForeignKey,
    IntegerChoices,
    SmallIntegerField,
    IntegerField,
    DateTimeField,
    BooleanField,
)

from shared.models import BaseModel
from users.models import User
from events.models import Event


class Order(BaseModel):
    class Status(IntegerChoices):
        PROCESSING = 1
        CANCELLED = 2
        CONFIRMED = 3

    user = ForeignKey(User, on_delete=PROTECT)
    status = SmallIntegerField(choices=Status, default=Status.PROCESSING)
    total = IntegerField()
    tax = IntegerField(null=True)

    class Meta:
        db_table = "orders"


class Payment(BaseModel):
    class Status(IntegerChoices):
        DUE = 1
        OVERDUE = 2
        CANCELLED = 3
        PAID = 4

    user = ForeignKey(User, on_delete=PROTECT)
    order = ForeignKey(Order, on_delete=PROTECT)
    status = SmallIntegerField(choices=Status, default=Status.DUE)
    amount = IntegerField()

    class Meta:
        db_table = "payments"


class Price(BaseModel):
    amount = IntegerField()
    event = ForeignKey(Event, on_delete=PROTECT)
    expiry = DateTimeField(null=True)
    max_uses = IntegerField(null=True)

    class Meta:
        db_table = "prices"


class Coupon(BaseModel):
    class DiscountType(IntegerChoices):
        PERCENTAGE = 1  # Discount over order total
        FIXED = 2  # Discount over order total
        SUBTOTAL_PERCENTAGE = 3  # Discount over order subtotal (Ticket price sum)
        SUBTOTAL_FIXED = 4  # Discount over order subtotal (Ticket price sum)

    amount = IntegerField()
    type = IntegerField(choices=DiscountType, default=DiscountType.FIXED)
    active = BooleanField(default=True)

    class Meta:
        db_table = "coupons"


class CouponUse(BaseModel):
    order = ForeignKey(Order, on_delete=PROTECT)
    coupon = ForeignKey(Coupon, on_delete=PROTECT)

    class Meta:
        db_table = "coupon_use"
