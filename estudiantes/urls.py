from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('agregar-alumno/', views.agregar_alumno, name="add_alumno"),
    path('agregar-asignatura/', views.agregar_asignatura, name="add_asignatura"),
    path('agregar-curso/', views.agregar_curso, name="add_curso"),
    path('agregar-profesor/', views.agregar_profesor, name="add_profesor"),
    path('agregar-asistencia/', views.agregar_asistencia, name="add_asistencia"),
    path('agregar-notas/', views.agregar_notas, name="add_nota"),
    path('listar-alumno/', views.listar_alumnos, name="list_alumnos"),
    path('listar-asignatura/', views.listar_asignaturas, name="list_asignaturas"),
    path('listar-curso/', views.listar_cursos, name="list_cursos"),
    path('listar-profesor/', views.listar_profesores, name="list_profesores"),
    path('listar-asistencia/', views.listar_asistencias, name="list_asistencias"),
    path('listar-nota/', views.listar_notas, name="list_notas"),
    path('modificar-alumno/<rut>/', views.modificar_alumno, name="modify_alumno"),
    path('modificar-profesor/<rut>/', views.modificar_profesor, name="modify_profesor"),
    path('modificar-asistencia/<id>/', views.modificar_asistencia, name="modify_asistencia"),
    path('modificar-curso/<nombreCurso>/', views.modificar_curso, name="modify_curso"),
    path('modificar-nota/<id>/', views.modificar_notas, name="modify_nota"),
    path('modificar-asignatura/<codigo>/', views.modificar_asignatura, name="modify_asignatura"),

    path('eliminar-alumno/<rut>/', views.eliminar_alumno, name="delete_alumno"),
    path('eliminar-profesor/<rut>/', views.eliminar_profesores, name="delete_profesor"),
    path('eliminar-asistencia/<id>/', views.eliminar_asistencia, name="delete_asistencia"),
    path('eliminar-curso/<nombreCurso>/', views.eliminar_curso, name="delete_curso"),
    path('eliminar-alumno/<id>/', views.eliminar_notas, name="delete_nota"),
    path('eliminar-asignatura/<codigo>/', views.eliminar_asignatura, name="delete_asignatura"),

]
