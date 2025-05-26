from rest_framework.routers import DefaultRouter
from .views import ProductoApiView

router = DefaultRouter()

router.register(
    r'productos',
    ProductoApiView,
    basename='productoss'
)

urlpatterns = router.urls