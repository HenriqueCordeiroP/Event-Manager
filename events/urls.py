from rest_framework.routers import DefaultRouter
from events.views import EventsViewSet

app_name = 'events'

router = DefaultRouter()
router.register(r'', EventsViewSet,)

urlpatterns = router.urls