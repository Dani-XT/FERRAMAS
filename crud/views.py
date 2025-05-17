from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UsuarioForm,ProductoForm, EditorialForm, TipoForm
from apps.front.home.models import Producto, Editorial, Tipo

#TODO: CRUD
def crud_home(request):
    return render(request, 'crud/crud_home.html')

#TODO: USUARIOS
def usuarios_list(request):
    usuarios = User.objects.all()
    context = {"usuarios": usuarios}
    return render(request, "usuarios/usuarios_list.html", context)

def usuarios_add(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            form = UsuarioForm()  
            context = {"mensaje": "Usuario guardado satisfactoriamente", "form": form}
            return render(request, "usuarios/usuarios_add.html", context)
    else:
        form = UsuarioForm()
    context = {"form": form}
    return render(request, "usuarios/usuarios_add.html", context)

def usuarios_del(request, pk):
    try:
        usuario = User.objects.get(pk=pk)
        usuario.delete()
        mensaje = "Usuario eliminado satisfactoriamente"
    except User.DoesNotExist:
        mensaje = "Error al eliminar el usuario"
    usuarios = User.objects.all()
    context = {"usuarios": usuarios, "mensaje": mensaje}
    return render(request, "usuarios/usuarios_list.html", context)

def usuarios_find_edit(request, pk):
    try:
        usuario = get_object_or_404(User, pk=pk)
        if request.method == "POST":
            form = UsuarioForm(request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                mensaje = "Usuario actualizado correctamente"
                context = {"mensaje": mensaje, "usuario": usuario, "form": form}
                return render(request, "usuarios/usuarios_edit.html", context)
        else:
            form = UsuarioForm(instance=usuario)
        context = {"usuario": usuario, "form": form}
        return render(request, "usuarios/usuarios_edit.html", context)
    except User.DoesNotExist:
        mensaje = "Error, el usuario no existe"
        context = {"mensaje": mensaje}
        return render(request, "usuarios/usuarios_edit.html", context)

def usuarios_update(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    mensaje = ""
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        print("Datos del formulario:", request.POST)  # Imprime los datos recibidos del formulario
        if form.is_valid():
            print("Formulario válido")
            form.save()
            mensaje = "Usuario actualizado correctamente"
            return redirect('usuarios_list')  # Redirige a la lista de usuarios después de actualizar
        else:
            print("Formulario no válido", form.errors)
            mensaje = "Error al actualizar el usuario: " + str(form.errors)
    else:
        form = UsuarioForm(instance=usuario)
    context = {"form": form, "usuario": usuario, "mensaje": mensaje}
    return render(request, "usuarios/usuarios_edit.html", context)

#TODO: PRODUCTOS
def productos_list(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, "productos/producto_list.html", context)

def productos_add(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos_list')
    else:
        form = ProductoForm()
    context = {"form": form}
    return render(request, "productos/producto_add.html", context)

def productos_del(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('productos_list')
    return render(request, "productos/producto_confirm_delete.html", {"producto": producto})

def productos_find_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos_list')
    else:
        form = ProductoForm(instance=producto)
    context = {"form": form, "producto": producto}
    return render(request, "productos/producto_edit.html", context)

#TODO: EDITORIALES
def editoriales_list(request):
    editoriales = Editorial.objects.all()
    context = {"editoriales": editoriales}
    return render(request, "editorial/editorial_list.html", context)

def editoriales_add(request):
    if request.method == "POST":
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('editoriales_list')
    else:
        form = EditorialForm()
    context = {"form": form}
    return render(request, "editorial/editorial_add.html", context)

def editoriales_del(request, pk):
    editorial = get_object_or_404(Editorial, pk=pk)
    if request.method == "POST":
        editorial.delete()
        return redirect('editoriales_list')
    return render(request, "editorial/editorial_confirm_delete.html", {"editorial": editorial})

def editoriales_find_edit(request, pk):
    editorial = get_object_or_404(Editorial, pk=pk)
    if request.method == "POST":
        form = EditorialForm(request.POST, instance=editorial)
        if form.is_valid():
            form.save()
            return redirect('editoriales_list')
    else:
        form = EditorialForm(instance=editorial)
    context = {"form": form, "editorial": editorial}
    return render(request, "editorial/editorial_edit.html", context)

#TODO: TIPOS
def tipos_list(request):
    tipos = Tipo.objects.all()
    context = {"tipos": tipos}
    return render(request, "tipo/tipo_list.html", context)

def tipos_add(request):
    if request.method == "POST":
        form = TipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipos_list')
    else:
        form = TipoForm()
    context = {"form": form}
    return render(request, "tipo/tipo_add.html", context)

def tipos_del(request, pk):
    tipo = get_object_or_404(Tipo, pk=pk)
    if request.method == "POST":
        tipo.delete()
        return redirect('tipos_list')
    return render(request, "tipo/tipo_confirm_delete.html", {"tipo": tipo})

def tipos_find_edit(request, pk):
    tipo = get_object_or_404(Tipo, pk=pk)
    if request.method == "POST":
        form = TipoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('tipos_list')
    else:
        form = TipoForm(instance=tipo)
    context = {"form": form, "tipo": tipo}
    return render(request, "tipo/tipo_edit.html", context)




