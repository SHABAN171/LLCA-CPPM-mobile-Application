from rest_framework.routers import DefaultRouter
from .views import LifecycleCostViewSet

router = DefaultRouter()
router.register(
    r'lcca',
    LifecycleCostViewSet,
    basename='lcca'
)

urlpatterns = router.urls