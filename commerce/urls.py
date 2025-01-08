from django.urls import path

from commerce.views import OrderRequestView

app_name = 'commerce'

urlpatterns = [
    path('', OrderRequestView.as_view(), name='order-request'),
]