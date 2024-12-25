from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UsersReadonlyViewSet

app_name = 'users'

router = DefaultRouter()
router.register(r'', UsersReadonlyViewSet,)

urlpatterns = router.urls