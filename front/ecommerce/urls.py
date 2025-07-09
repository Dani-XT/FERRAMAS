from django.urls import path

# Views personalizados
from front.ecommerce.ecommerce_list.views import EcommerceListView
from front.ecommerce.ecommerce_detail.views import EcommerceDetailView


urlpatterns = [
    path(
        "ecommerce/product/list/",
        EcommerceListView.as_view(template_name="ecommerce_list.html"),
        name="ecommerce-list",
    ),
    path(
        "ecommerce/product/<int:pk>/",
        EcommerceDetailView.as_view(template_name="ecommerce_detail.html"),
        name="ecommerce-detail",
    )
]

