from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer

class UsersReadonlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer