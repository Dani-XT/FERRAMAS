from django.urls import path
from . import views

urlpatterns = [
    #CRUD
    path('', views.crud_home, name='crud_home'),
    path('editoriales/', views.editoriales_list, name='editoriales_list'),
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('productos/', views.productos_list, name='productos_list'),
    path('tipos/', views.tipos_list, name='tipos_list'),

    #PRODUCTOS

    path('productos/', views.productos_list, name='productos_list'),
    path('productos/agregar/', views.productos_add, name='productos_add'),
    path('productos/<int:pk>/eliminar/', views.productos_del, name='productos_del'),
    path('productos/<int:pk>/editar/', views.productos_find_edit, name='productos_find_edit'),

    # Usuarios
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('usuarios/crear/', views.usuarios_add, name='usuarios_add'),
    path('usuarios/<int:pk>/eliminar/', views.usuarios_del, name='usuarios_del'),
    path('usuarios/<int:pk>/editar/', views.usuarios_find_edit, name='usuarios_find_edit'),
    path('usuarios/<int:pk>/actualizar/', views.usuarios_update, name='usuarios_update'),  # Aquí incluimos el pk

    #EDITORIAL

    path('editorial/', views.editoriales_list, name='editoriales_list'),
    path('editorial/agregar/', views.editoriales_add, name='editoriales_add'),
    path('editorial/<int:pk>/eliminar/', views.editoriales_del, name='editoriales_del'),
    path('editorial/<int:pk>/editar/', views.editoriales_find_edit, name='editoriales_find_edit'),

    #Tipo

    path('tipo/', views.tipos_list, name='tipos_list'),
    path('tipo/agregar/', views.tipos_add, name='tipos_add'),
    path('tipo/<int:pk>/eliminar/', views.tipos_del, name='tipos_del'),
    path('tipo/<int:pk>/editar/', views.tipos_find_edit, name='tipos_find_edit'),

]