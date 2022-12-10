from django.urls import path

from MiApp  import views

urlpatterns = [
    path('mostrar_curso/', views.mostrar_curso, name='Mostrar Curso'),
    path('about/', views.mostrar_about,  name='About'),
    path('', views.mostrar_index, name='Home'),
    path('mostrar_instructor/', views.mostrar_instructor, name='Mostrar Instructor'),
    path('crear_curso/', views.crear_curso, name='Crear Curso'),
    path('crear_instructor/', views.crear_instructor, name='Crear Instructor'),
    path('buscar_comision/', views.buscar_comision, name='Buscar Comision'),
    path('buscar_instructor/', views.buscar_instructor, name='Buscar Instructor'),
    path('mostrar_instructores/', views.mostrar_instructores, name='Mostrar Instructores'),
    path('eliminar_instructor/<instructor_id>', views.eliminar_instructor, name='Eliminar instructor'),
    path('actualizar_instructor/<instructor_id>', views.actualizar_instructor, name='actualizar instructor'),
    path('cursos_list/', views.CursoList.as_view(), name='List'),
    path('curso_detail/<pk>', views.CursoDetailView.as_view(), name='Detail'),
    path('curso_confirm_delete/<pk>', views.CursoDeleteView.as_view(), name='Delete'),
    path('curso_edit/<pk>', views.CursoUpdateView.as_view(), name='Update'),
    path('curso_form/', views.CursoCreateView.as_view(), name='Create'),
    path('signup/', views.SignUpView.as_view(), name='Sign Up'),
    path('login/', views.AdminLoginView.as_view(), name='Login'),
    path('logout/', views.AdminLogoutView.as_view(), name='Logout'),
    path('editar_usuario/', views.editar_usuario, name='Editar Usuario'),
]
