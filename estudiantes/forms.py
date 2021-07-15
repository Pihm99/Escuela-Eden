from django import forms
from .models import Alumno, Profesor, Nota, Asignatura, Asistencia, Curso


class AlumnoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellido"

    class Meta:
        model = Alumno

        fields = [
            "first_name",
            "last_name",
            "rut",
            "tipo",
            "email",
            "password",
        ]

        widgets = {
            "password": forms.PasswordInput(),
        }


class AlumnoUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AlumnoUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellido"

    class Meta:
        model = Alumno

        fields = [
            "first_name",
            "last_name",
            "rut",
            "tipo",
            "email",
        ]


class ProfesorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfesorForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellido"

    class Meta:
        model = Profesor

        fields = ["first_name",
                  "last_name",
                  "rut",
                  "tipo",
                  "email",
                  "password",
                  "asignatura",
                  "is_teacher",
                  ]

        widgets = {
            "password": forms.PasswordInput(),
        }


class ProfesorUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfesorUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellido"

    class Meta:
        model = Profesor

        fields = ["first_name",
                  "last_name",
                  "rut",
                  "tipo",
                  "email",
                  "asignatura",
                  "is_teacher",
                  ]


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota

        fields = [
            "alumno",
            "asignatura",
            "nota_1",
            "nota_2",
            "nota_3",
            "nota_4",
            "nota_5",
            "nota_6",
        ]

        widgets = {
            "nota_1": forms.NumberInput(attrs={"min": 1.0, "max": 7.0, "step": "0.1"}),
            "nota_2": forms.NumberInput(attrs={"min": 1.0, "max": 7.0, "step": "0.1"}),
            "nota_3": forms.NumberInput(attrs={"min": 1.0, "max": 7.0, "step": "0.1"}),
            "nota_4": forms.NumberInput(attrs={"min": 1.0, "max": 7.0, "step": "0.1"}),
            "nota_5": forms.NumberInput(attrs={"min": 1.0, "max": 7.0, "step": "0.1"}),
            "nota_6": forms.NumberInput(attrs={"min": 1.0, "max": 7.0, "step": "0.1"}),
        }


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso

        fields = ["nombreCurso",
                  "alumnos"]


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia

        fields = ["alumno",
                  "asignatura",
                  "fecha",
                  "asistencia"]

        widgets = {
            "fecha": forms.SelectDateWidget()
        }


class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura

        fields = '__all__'
# Terminar de configurar las formas y hacer las vistas, añadir las urls, crear los html
