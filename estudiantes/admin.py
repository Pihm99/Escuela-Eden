from django.contrib import admin
from .models import Alumno, Asignatura, Asistencia, Curso, Nota, Profesor, Usuario

admin.site.register(Alumno)
admin.site.register(Asignatura)
admin.site.register(Asistencia)
admin.site.register(Curso)
admin.site.register(Nota)
admin.site.register(Profesor)
admin.site.register(Usuario)
