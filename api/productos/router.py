from rest_framework.routers import DefaultRouter
from .views import ProductoListAPIView

router = DefaultRouter()

router.register(
    r'productos',
    ProductoListAPIView,
    basename='productos'
)

urlpatterns = router.urls