from django.urls import path, include

from auth.views import UserRegistrationView, TokenObtainPairAndUserIdView, UserIdAndTokenRefreshView

app_name = "auth"


urlpatterns = [
    path("sign-up/", UserRegistrationView.as_view(), name="sign-up"),
    path("sign-in/", TokenObtainPairAndUserIdView.as_view(), name="sign-in"),
    path("refresh-token/", UserIdAndTokenRefreshView.as_view(), name="refresh-token"),
]
