from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfesorForm, AlumnoForm, AsistenciaForm, CursoForm, NotaForm, AsignaturaForm, AlumnoUpdateForm,\
    ProfesorUpdateForm
from .models import Alumno, Asignatura, Asistencia, Profesor, Curso, Nota
from django.contrib.auth.decorators import login_required
from .decorators import admin_required, profesor_required
from django.contrib import messages


success = "Guardado correctamente"


# Create your views here.

def home(request):
    context = {

    }
    return render(request, 'estudiantes/public/index.html', context)


@login_required
@admin_required
def agregar_alumno(request):
    datos = {
        'form': AlumnoForm()
    }

    if request.method == "POST":
        formulario = AlumnoForm(request.POST)
        if formulario.is_valid():

            usertmp = formulario.save()
            usertmp.set_password(usertmp.password)
            usertmp.save()
            formulario.save()
            messages.success(request, "Agregado correctamente")
            return redirect('list_alumnos')
        else:
            datos["form"] = formulario

    return render(request, 'estudiantes/admin/alumnos/agregarAlumnos.html', datos)


@login_required
@admin_required
def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    datos = {
        'alumnos': alumnos
    }
    return render(request, 'estudiantes/admin/alumnos/listarAlumnos.html', datos)


@login_required
@admin_required
def modificar_alumno(request, rut):
    alumno = get_object_or_404(Alumno, rut=rut)
    datos = {
        'form': AlumnoUpdateForm(instance=alumno),
    }

    if request.method == "POST":
        formulario = AlumnoUpdateForm(data=request.POST, instance=alumno)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado correctamente")
            return redirect('list_alumnos')
        datos["form"] = formulario
    return render(request, 'estudiantes/admin/alumnos/modificarAlumnos.html', datos)


@admin_required
def eliminar_alumno(request, rut):
    alumno = get_object_or_404(Alumno, rut=rut)
    alumno.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect('list_alumnos')


@login_required
@admin_required
def agregar_profesor(request):
    datos = {
        'form': ProfesorForm()
    }

    if request.method == "POST":
        formulario = ProfesorForm(request.POST)
        if formulario.is_valid():
            usertmp = formulario.save()
            usertmp.set_password(usertmp.password)
            usertmp.save()
            formulario.save()
            messages.success(request, "Agregado correctamente")
            return redirect('list_profesores')
        else:
            datos["form"] = formulario

    return render(request, 'estudiantes/admin/profesores/agregarProfesor.html', datos)


@login_required
@admin_required
def listar_profesores(request):
    profesores = Profesor.objects.all()
    datos = {
        'profesores': profesores
    }
    return render(request, 'estudiantes/admin/profesores/listarProfesores.html', datos)


@login_required
@admin_required
def modificar_profesor(request, rut):
    profesor = get_object_or_404(Profesor, rut=rut)
    datos = {
        'form': ProfesorForm(instance=profesor),
    }

    if request.method == "POST":
        formulario = ProfesorForm(data=request.POST, instance=profesor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado correctamente")
            return redirect('list_profesores')
        datos["form"] = formulario
    return render(request, 'estudiantes/admin/profesores/modificarProfesor.html', datos)


@admin_required
def eliminar_profesores(request, rut):
    profesor = get_object_or_404(Profesor, rut=rut)
    profesor.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect('list_profesores')


@login_required
@profesor_required
def agregar_asistencia(request):
    datos = {
        'form': AsistenciaForm()
    }

    instancia_usuario = Profesor.objects.get(email__exact=request.user.email)

    if request.method == "POST":
        formulario = AsistenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
            return redirect('list_asistencias')

        else:
            datos["form"] = formulario

    return render(request, 'estudiantes/private/asistencia/agregarAsistencia.html', datos)


@login_required
@profesor_required
def listar_asistencias(request):

    usuario = request.user
    if usuario.tipo == "Profesor":
        asign = usuario.asignatura
        asistencias = Asistencia.objects.filter(asignatura__nombreAsignatura__exact=asign)
    else:
        asistencias = Asistencia.objects.all()

    datos = {
        'asistencias': asistencias
    }
    return render(request, 'estudiantes/private/asistencia/listarAsistencia.html', datos)


@login_required
@profesor_required
def modificar_asistencia(request, id):
    asistencia = get_object_or_404(Asistencia, id=id)
    datos = {
        'form': AsistenciaForm(instance=asistencia),
    }

    if request.method == "POST":
        formulario = AsistenciaForm(data=request.POST, instance=asistencia)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado correctamente")
            return redirect('list_asistencias')
        datos["form"] = formulario
    return render(request, 'estudiantes/private/asistencia/modificarAsistencia.html', datos)


@profesor_required
@admin_required
def eliminar_asistencia(request, id):
    asistencia = get_object_or_404(Asistencia, id=id)
    asistencia.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect('list_asistencias')


@login_required
@admin_required
def agregar_curso(request):
    datos = {
        'form': CursoForm()
    }

    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
            return redirect('list_cursos')
        else:
            datos["form"] = formulario

    return render(request, 'estudiantes/admin/cursos/agregarCurso.html', datos)


@login_required
@admin_required
def listar_cursos(request):
    cursos = Curso.objects.all()
    datos = {
        'cursos': cursos,
    }
    return render(request, 'estudiantes/admin/cursos/listarCursos.html', datos)


@login_required
@admin_required
def modificar_curso(request, nombreCurso):
    curso = get_object_or_404(Curso, nombreCurso=nombreCurso)
    datos = {
        'form': CursoForm(instance=curso),
    }

    if request.method == "POST":
        formulario = CursoForm(data=request.POST, instance=curso)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado correctamente")
            return redirect('list_cursos')
        datos["form"] = formulario
    return render(request, 'estudiantes/admin/cursos/modificarCurso.html', datos)


@admin_required
def eliminar_curso(request, nombreCurso):
    curso = get_object_or_404(Curso, nombreCurso=nombreCurso)
    curso.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect('list_cursos')


@login_required
@profesor_required
def agregar_notas(request):
    datos = {
        'form': NotaForm()
    }

    if request.method == "POST":
        formulario = NotaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
            return redirect('list_notas')
        else:
            datos["form"] = formulario

    return render(request, 'estudiantes/private/notas/agregarNotas.html', datos)


@login_required
def listar_notas(request):
    usuario = request.user
    if usuario.tipo == "Estudiante":
        rut = usuario.rut
        notas = Nota.objects.filter(alumno__rut__exact=rut)
    elif usuario.tipo == "Profesor":
        asign = usuario.asignatura.nombreAsignatura
        notas = Nota.objects.filter(asignatura__nombreAsignatura__exact=asign)
    else:
        notas = Nota.objects.all()

    datos = {
        'notas': notas
    }
    return render(request, 'estudiantes/private/notas/listarNotas.html', datos)


@login_required
@profesor_required
def modificar_notas(request, id):
    nota = get_object_or_404(Nota, id=id)
    datos = {
        'form': NotaForm(instance=nota),
    }

    if request.method == "POST":
        formulario = NotaForm(data=request.POST, instance=nota)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado correctamente")
            return redirect('list_notas')
        datos["form"] = formulario
    return render(request, 'estudiantes/private/notas/modificarNotas.html', datos)


@profesor_required
@admin_required
def eliminar_notas(request, id):
    nota = get_object_or_404(Nota, id=id)
    nota.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect('list_notas')


@login_required
@admin_required
def agregar_asignatura(request):
    datos = {
        'form': AsignaturaForm()
    }

    if request.method == "POST":
        formulario = AsignaturaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
            return redirect('list_asignaturas')
        else:
            datos["form"] = formulario

    return render(request, 'estudiantes/admin/asignatura/agregarAsignatura.html', datos)


@login_required
@admin_required
def listar_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    datos = {
        'asignaturas': asignaturas
    }
    return render(request, 'estudiantes/admin/asignatura/listarAsignaturas.html', datos)


@login_required
@admin_required
def modificar_asignatura(request, codigo):
    asignatura = get_object_or_404(Asignatura, codigo=codigo)
    datos = {
        'form': AsignaturaForm(instance=asignatura),
    }

    if request.method == "POST":
        formulario = AsignaturaForm(data=request.POST, instance=asignatura)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado correctamente")
            return redirect('list_asignaturas')
        datos["form"] = formulario
    return render(request, 'estudiantes/admin/asignatura/modificarAsignatura.html', datos)


@admin_required
def eliminar_asignatura(request, codigo):
    asignatura = get_object_or_404(Asignatura, codigo=codigo)
    asignatura.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect('list_asignaturas')

