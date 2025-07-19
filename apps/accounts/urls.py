from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.accounts.views import AccountsView
from apps.usuarios.views import UsuariosView

urlpatterns = [
    path(
        "accounts/",
        login_required(AccountsView.as_view(template_name="view/user_accounts.html")),
        name="accounts",
    ),
    path(
        "accounts/update/<int:pk>/",
        login_required(AccountsView.as_view(template_name="view/user_accounts.html")),
        name="accounts-update",
    ),
    # PRUEBA
        path(
        "app/user/list/",
        login_required(AccountsView.as_view(template_name="detail/app_user_list.html")),
        name="app-user-list",
    ),
    path(
        "app/user/view/account/",
        login_required(AccountsView.as_view(template_name="detail/app_user_view_account.html")),
        name="app-user-view-account",
    ),
    path(
        "app/user/view/security/",
        login_required(AccountsView.as_view(template_name="detail/app_user_view_security.html")),
        name="app-user-view-security",
    ),
    path(
        "app/user/view/billing/",
        login_required(AccountsView.as_view(template_name="detail/app_user_view_billing.html")),
        name="app-user-view-billing",
    ),
    path(
        "app/user/view/notifications/",
        login_required(AccountsView.as_view(template_name="detail/app_user_view_notifications.html")),
        name="app-user-view-notifications",
    ),
    path(
        "app/user/view/connections/",
        login_required(AccountsView.as_view(template_name="detail/app_user_view_connections.html")),
        name="app-user-view-connections",
    ),
]