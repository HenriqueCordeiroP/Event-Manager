from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from django.utils import timezone
from django.db.models import OuterRef, Subquery, Count

from commerce.serializers import OrderRequestSerializer
from commerce.models import Order, Payment
from tickets.models import Ticket

# Create Order
# Receives Event and Users[]
# Requesting user is responsible for Order
# If Free
# Create Order, Payment and Ticket 100% confirmed
# If Paid
# Receives Payment Token Id, Coupon, Installments
# Calculate total, Create Order, Payment and Ticked Pending
# Once Order is 100% paid, ticket is confirmed

# Self-authorization
# Tickets are shown for their respective users
# Order shows all tickets

# Validate Coupon
# Get user orders
# Create Prices


@extend_schema(tags=["Commerce"])
class OrderRequestView(APIView):
    serializer_class = OrderRequestSerializer
    permission_classes = [IsAuthenticated]

    def serialize(self, request):
        serializer = self.serializer_class(data=request.data)
        return serializer

    def post(self, request):
        serializer = self.serialize(request)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data

        price = data.price
        accountable_user = request.user
        users = data.users

        price_uses = Ticket.objects.filter(price=price).count()

        if price.max_uses and price_uses >= price.max_uses:
            return Response(
                {"price": "The selected price has reached its usage limit"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if price.max_uses and price_uses + len(users) >= price.max_uses:
            return Response(
                {
                    "price": "There are not enough available items of this price for the requested amount of users"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        is_free_event = price.amount == 0

        if is_free_event:
            order = Order.objects.create(
                user=accountable_user, status=Order.Status.CONFIRMED, total=0
            )
            Payment.objects.create(
                user=accountable_user, order=order, status=Payment.Status.PAID, amount=0
            )

            for user in users:
                Ticket.objets.create(
                    user=user, event=price.event, order=order, price=price
                )

            return Response(
                {"created": "Tickets created successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            order = Order.objects.create(
                user=accountable_user, status=Order.Status.PROCESSING, total=price.amount
            )
            
            # TODO create payment via webhook and tickets upon payment // third party gatway e.g. Stripe

            return Response(
                {"payment pending": "Tickets will be created upon payment"},
                status=status.HTTP_202_ACCEPTED,
            )
