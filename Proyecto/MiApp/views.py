from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from MiApp.models import Curso, Instructor, Avatar
from .forms import CrearCursoForm, CrearinstructorForm, SignUpForm, UserEditForm

# Redireccion
from django.urls import reverse_lazy
# Auth
from django.contrib.auth.views import LoginView, LogoutView

#Los decoradores sirven para funciones > vistas basadas en funciones
from django.contrib.auth.decorators import login_required
#Los mixins sirven para clases > vistas basadas en clases
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def mostrar_curso(request):

    c1 = Curso(nombre='Programador', comision='2022')
    c2 = Curso(nombre='Programador Web', comision='2022')

    return render(request, 'MiApp/curso.html', {'curso':[c1, c2]})

def mostrar_instructor(request):
    i1= Instructor(nombre='Ignacio', apellido='Giordano', email='ignaciogiordano03@gmail.com', profesion='Programador')
    i2= Instructor(nombre='Monica', apellido='Cora',  email='niquitacora53@gmail.com', profesion='Docente')

    return render(request, 'MiApp/instructor.html', {'instructor':[i1, i2]})

#@login_required
def mostrar_index(request):

    imagenes = Avatar.objects.filter(user=request.user.id)

    return render(request, 'MiApp/index.html') #{'url': imagenes[0].imagen.url}

def mostrar_about(request):

    return render(request, 'MiApp/about.html')


def crear_curso(request):

    if request.method == 'POST':

        formulario = CrearCursoForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            curso = Curso(nombre=formulario_limpio['nombre'], comision=formulario_limpio['comision'])

            curso.save()

            return render(request, 'MiApp/index.html')
    else:
        formulario = CrearCursoForm()
    
    return render(request, 'MiApp/crear_curso.html', {'formulario': formulario})      

def crear_instructor(request):
    if request.method == 'POST':

        formulario = CrearinstructorForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            instructor = Instructor(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], email=formulario_limpio['email'], profesion=formulario_limpio['profesion']) 

            instructor.save()

            return render(request, 'MiApp/index.html')
    else: 
        formulario = CrearinstructorForm()
        
        return render(request, 'MiApp/crear_instructor.html', {'formulario': CrearinstructorForm})

def buscar_comision(request):

    if request.GET.get('comision', False): # -> 12345
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)

        return render(request, 'MiApp/buscar_comision.html', {'cursos': cursos})
    else:
        respuesta = 'No hay datos'
    return render(request, 'MiApp/buscar_comision.html', {'respuesta': respuesta})

def buscar_instructor(request):

    if request.GET.get('email', False):
        email = request.GET['email']
        instructores = Instructor.objects.filter(email__icontains=email)

        return render(request, 'MiApp/buscar_instructor.html', {'instructores': instructores})
    else:
        respuesta = 'No hay datos'
    return render(request, 'MiApp/buscar_instructor.html', {'respuesta': respuesta})

def mostrar_instructores(request):

    instructores = Instructor.objects.all()

    context = {'instructores': instructores}

    return render(request, 'MiApp/mostrar_instructores.html', context=context)
    
def eliminar_instructor(request, instructor_id):

    instructor = Instructor.objects.get(id=instructor_id)

    instructor.delete()


    instructores = Instructor.objects.all()

    context = {'instructores': instructores}

    return render(request, 'MiApp/mostrar_instructores.html', context=context)


def actualizar_instructor(request, instructor_id):

    instructor = Instructor.objects.get(id=instructor_id)
    
    if request.method == 'POST':

        formulario = CrearinstructorForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            instructor.nombre = formulario_limpio ['nombre']   
            instructor.apellido = formulario_limpio ['apellido'] 
            instructor.email = formulario_limpio ['email'] 
            instructor.profesion = formulario_limpio ['profesion'] 
            
            
            instructor.save()

            return render(request, 'MiApp/index.html')
    else: 
        formulario = CrearinstructorForm(initial={'nombre': instructor.nombre, 'apellido': instructor.apellido, 'email': instructor.email, 'profesion': instructor.profesion})
        
    return render(request, 'MiApp/actualizar_instructor.html', {'formulario': CrearinstructorForm, 'instructor': instructor })  

def editar_usuario(request):

    usuario = request.user

    if request.method == 'POST':
        usuario_form = UserEditForm(request.POST)

        if usuario_form.is_valid():

            informacion = usuario_form.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request, 'MiApp/index.html')

    else:
        usuario_form = UserEditForm(initial={
            'username': usuario.username,
            'email': usuario.email,
        })

    return render(request, 'MiApp/admin_update.html', {
        'form': usuario_form,
        'usuario': usuario
    })


class CursoList(LoginRequiredMixin, ListView):

    model = Curso
    template_name = 'MiApp/cursos_list.html' 


class CursoDetailView(DetailView):

    model = Curso
    template_name = 'MiApp/curso_detalle.html'

class CursoDeleteView(DeleteView):

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('cursos_list/', views.CursoList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash
    model = Curso
    success_url = '/cursos_list'

class CursoUpdateView(UpdateView):

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('cursos_list/', views.CursoList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash
    model = Curso
    success_url = '/cursos_list'
    fields = ['nombre', 'comision']

class CursoCreateView(LoginRequiredMixin, CreateView):

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('cursos_list/', views.CursoList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash
    model = Curso
    success_url = '/cursos_list'
    fields = ['nombre', 'comision']

class SignUpView(CreateView):

    form_class = SignUpForm
    success_url = reverse_lazy('Home')
    template_name = 'MiApp/registro.html'

class AdminLoginView(LoginView):
    template_name = 'MiApp/login.html'

class AdminLogoutView(LogoutView):
    template_name = 'MiApp/logout.html'

class AdminUpdateView(UpdateView):

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('cursos_list/', views.CursoList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash
    model = Curso
    success_url = '/cursos_list'
    fields = ['nombre', 'comision']