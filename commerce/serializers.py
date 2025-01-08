from rest_framework.serializers import (
    Serializer,
    PrimaryKeyRelatedField,
    CharField,
    IntegerField,
)
from django.utils import timezone

from users.models import User
from commerce.models import Price, Coupon


class OrderRequestSerializer(Serializer):
    price = PrimaryKeyRelatedField(
        queryset=Price.objects.filter(expiry__gte=timezone.now()),
        many=False,
        error_messages={
            "does_not_exist": "Price not found.",
            "invalid": "Invalid price key provided.",
        },
    )
    users = PrimaryKeyRelatedField(
        queryset=User.objects.filter(is_active=True, is_deleted=False),
        many=True,
        error_messages={
            "does_not_exist": "User not found.",
            "invalid": "Invalid user key provided.",
        },
    )
    payment_token = CharField(max_length=20, required=False)
    coupon = PrimaryKeyRelatedField(
        queryset=Coupon.objects.all(),
        many=False,
        required=False,
        error_messages={
            "does_not_exist": "Coupon not found.",
            "invalid": "Invalid coupon key provided.",
        },
    )
    installments = IntegerField(default=1, required=False)
