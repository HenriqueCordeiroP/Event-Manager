from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth.views import UserRegistrationView

app_name = "auth"


urlpatterns = [
    path("sign-up/", UserRegistrationView.as_view(), name="sign-up"),
    path("sign-in/", TokenObtainPairView.as_view(), name="sign-in"),
    path("refresh-token/", TokenRefreshView.as_view(), name="refresh-token"),
]
