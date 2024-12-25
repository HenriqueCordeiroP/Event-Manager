from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema

from auth.serializers import UserRegistrationSerializer, TokenObtainPairAndUserIdSerializer, UserIdAndTokenRefreshSerializer

@extend_schema(tags=["Authentication"])
class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    serializer_class=UserRegistrationSerializer

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'email': user.email,
                'name': user.name
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(tags=["Authentication"])
class TokenObtainPairAndUserIdView(TokenObtainPairView):
    serializer_class = TokenObtainPairAndUserIdSerializer

@extend_schema(tags=["Authentication"])
class UserIdAndTokenRefreshView(TokenRefreshView):
    serializer_class = UserIdAndTokenRefreshSerializer