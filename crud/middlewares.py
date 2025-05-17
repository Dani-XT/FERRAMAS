from django.shortcuts import redirect
from django.urls import reverse

class AdminAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/crud/'):
            if not request.user.is_authenticated or not request.user.is_staff:
                # Si el usuario no está autenticado o no es staff, redirigir a la página de inicio de sesión de administración
                return redirect(reverse('admin:index'))
        
        response = self.get_response(request)
        return response
