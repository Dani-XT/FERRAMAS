from django.urls import path
from django.contrib.auth.decorators import login_required

# Views personalizados
# -------------------------------------------------------
# TODO: MODALES
# -------------------------------------------------------
from apps.utils.views import get_modal_icono
# -------------------------------------------------------
# TODO: CALCULOS
# -------------------------------------------------------

# -------------------------------------------------------
# TODO: COMPONENTES
# -------------------------------------------------------
from apps.utils.views import select_obtener_ubicacion, get_permisos_por_contenttype

app_name = "utils"

urlpatterns = [
    # -------------------------------------------------------
    # TODO: MODALES
    # -------------------------------------------------------
    # iconos
    path(
        "modal/icon/", 
        get_modal_icono, 
        name="modal-iconos"
    ),
    path(
        "modal/icon/<str:icon_selected>/",
        get_modal_icono,
        name="modal-iconos"
    ),
    # -------------------------------------------------------
    # TODO: CALCULOS
    # -------------------------------------------------------

    # -------------------------------------------------------
    # TODO: COMPONENTES
    # -------------------------------------------------------
    path(
        "obtener-ubicacion/", 
        select_obtener_ubicacion, 
        name="obtener-ubicacion"
    ),
    path(
        "get_permisos_por_contenttype/",
        login_required(get_permisos_por_contenttype), 
        name="get-permisos-por-contenttype" 
    )
]