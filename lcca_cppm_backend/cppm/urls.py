from rest_framework.routers import DefaultRouter
from .views import PortfolioAnalysisViewSet

router = DefaultRouter()
router.register(
    r'cppm',
    PortfolioAnalysisViewSet,
    basename='cppm'
)

urlpatterns = router.urls