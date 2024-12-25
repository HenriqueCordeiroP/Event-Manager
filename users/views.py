from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from users.models import User
from users.serializers import UserSerializer

@extend_schema(tags=["Users"])
class UsersReadonlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
