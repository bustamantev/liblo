from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from .forms import SignupForm, LibroForm, LibroModificacionForm, CustomUserForm, CustomUserModificacionForm
from .models import CategoriaLibro, Libro, CustomUser
from django.contrib import messages

NOMBRE_DEL_SITIO = 'Librotek'
# @login_required
def titulo(subtitulo=None):
    if subtitulo is None:
        return NOMBRE_DEL_SITIO
    return f'{NOMBRE_DEL_SITIO} - {subtitulo}'

# Views
@login_required
def index(request):
    return render(request, 'core/index.html',
        {
            'titulo': titulo(),
            'subtitulo': 'Bienvenidos a Librotek'
        }
    )

def historia(request):
    categoria_historia = CategoriaLibro.objects.get(nombre='Historia')
    libros = Libro.objects.filter(categoria=categoria_historia)
    return render(request, 'core/categoria.html', {'libros': libros})

def fantasia(request):
    categoria_fantasia = CategoriaLibro.objects.get(nombre='Fantasía')
    libros = Libro.objects.filter(categoria=categoria_fantasia)
    return render(request, 'core/categoria.html', {'libros': libros})

def psicologia(request):
    categoria_psicologia = CategoriaLibro.objects.get(nombre='Psicología')
    libros = Libro.objects.filter(categoria=categoria_psicologia)
    return render(request, 'core/categoria.html', {'libros': libros})

def manuales(request):
    categoria_manuales = CategoriaLibro.objects.get(nombre='Manuales')
    libros = Libro.objects.filter(categoria=categoria_manuales)
    return render(request, 'core/categoria.html', {'libros': libros})

def novelas(request):
    categoria_novelas = CategoriaLibro.objects.get(nombre='Novelas')
    libros = Libro.objects.filter(categoria=categoria_novelas)
    return render(request, 'core/categoria.html', {'libros': libros})


def crear_perfil(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        nombre_usuario = request.POST.get('nombre_usuario')
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')
        direccion = request.POST.get('direccion')

        # Crear un nuevo usuario en el modelo User
        user = User.objects.create_user(username=nombre_usuario, email=email, password=contrasena)

        # Crear un nuevo perfil asociado al usuario
        perfil = Perfil.objects.create(
            usuario=user,
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            nombre_usuario=nombre_usuario,
            email=email,
            contrasena=contrasena,
            direccion=direccion
        )

        return redirect('lista_usuarios')
    return render(request, 'core/crear_perfil.html')

# Vista para listar todos los usuarios
@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    perfiles = Perfil.objects.all()
    context = {
        'usuarios': usuarios,
        'perfiles': perfiles
    }
    return render(request, 'core/lista_usuarios.html', context)

# Vista para actualizar un perfil
@login_required
def actualizar_perfil(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == 'POST':
        perfil.nombre = request.POST.get('nombre')
        perfil.apellido = request.POST.get('apellido')
        perfil.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        perfil.nombre_usuario = request.POST.get('nombre_usuario')
        perfil.email = request.POST.get('email')
        perfil.contrasena = request.POST.get('contrasena')
        perfil.direccion = request.POST.get('direccion')
        perfil.save()
        return redirect('lista_usuarios')
    context = {
        'perfil': perfil
    }
    return render(request, 'core/actualizar_perfil.html', context)

# Vista para eliminar un perfil
@login_required
def eliminar_perfil(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == 'POST':
        perfil.delete()
        return redirect('lista_usuarios')
    context = {
        'perfil': perfil
    }
    return render(request, 'core/eliminar_perfil.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')  # Redirige al usuario a la página de inicio de sesión después del registro
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def lista_usuarios(request):
    order_by = request.GET.get('order_by', 'username')
    order_dir = request.GET.get('order_dir', 'asc')

    if order_dir == 'desc':
        order_by = '-' + order_by

    usuarios = CustomUser.objects.order_by(order_by)

    context = {
        'usuarios': usuarios,
        'order_by': order_by,
        'order_dir': order_dir,
    }
    return render(request, 'core/lista_usuarios.html', context)

def crear_usuario(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            username_usuario = usuario.username
            messages.success(request, f'Usuario "{username_usuario}" creado correctamente.')
            return redirect('/lista/usuarios/')
    else:
        form = CustomUserForm()
    return render(request, 'core/form_usuario.html', {'form': form})

def modificar_usuario(request, usuario_id):
    usuario = get_object_or_404(CustomUser, pk=usuario_id)
    
    if request.method == 'POST':
        form = CustomUserModificacionForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario_modificado = form.save(commit=False)
            usuario_modificado.save()
            username_usuario = usuario_modificado.username
            messages.success(request, f'Usuario "{username_usuario}" modificado correctamente.')
            return redirect('/lista/usuarios/')
    else:
        form = CustomUserModificacionForm(instance=usuario)
    
    return render(request, 'core/form_mod_usuario.html', {'form': form})

def eliminar_usuario(request, usuario_id):
    try:
        usuario = get_object_or_404(CustomUser, id=usuario_id)
        username_usuario = usuario.username
        usuario.delete()
        messages.success(request, f'Usuario "{username_usuario}" eliminado correctamente.')
    except:
        messages.error(request, 'Error al eliminar el usuario.')
    return redirect('/lista/usuarios/')

def lista_libros(request):
    # Obtener el parámetro de orden y establecer el orden predeterminado
    order_by = request.GET.get('order_by', 'categoria__nombre')
    # Obtener el parámetro de dirección de orden y establecer el orden predeterminado
    order_dir = request.GET.get('order_dir', 'asc')

    # Cambiar el orden a descendente si se especifica
    if order_dir == 'desc':
        order_by = '-' + order_by

    # Obtener la lista de libros ordenada
    libros = Libro.objects.order_by(order_by)

    context = {
        'libros': libros,
        'order_by': order_by,
        'order_dir': order_dir,
    }
    return render(request, 'core/lista_libros.html', context)

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            titulo_libro = libro.titulo  # Obtener el título del libro recién creado
            messages.success(request, f'Libro "{titulo_libro}" creado correctamente.')
            return redirect('/lista/libros/')
    else:
        form = LibroForm()
    return render(request, 'core/form_libro.html', {'form': form})

def modificar_libro(request, libro_id):
    # Obtener el libro específico
    libro = get_object_or_404(Libro, pk=libro_id)
    
    if request.method == 'POST':
        # Si se envió el formulario, procesar los datos
        form = LibroModificacionForm(request.POST, instance=libro)
        if form.is_valid():
            libro_modificado = form.save(commit=False)  # Guardar el libro modificado sin hacer commit todavía
            libro_modificado.save()
            titulo_libro = libro_modificado.titulo  # Obtener el título del libro modificado
            messages.success(request, f'Libro "{titulo_libro}" modificado correctamente.')
            return redirect('/lista/libros/')
    else:
        # Si es una solicitud GET, mostrar el formulario pre-rellenado con los datos del libro
        form = LibroModificacionForm(instance=libro)
    
    return render(request, 'core/form_mod_libro.html', {'form': form})

def eliminar_libro(request, libro_id):
    try:
        libro = get_object_or_404(Libro, id=libro_id)
        titulo_libro = libro.titulo  # Obtener el título del libro antes de eliminarlo
        libro.delete()
        messages.success(request, f'Libro "{titulo_libro}" eliminado correctamente.')
    except:
        messages.error(request, 'Error al eliminar el libro.')
    return redirect('/lista/libros/')