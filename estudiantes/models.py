from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, rut, email, password=None, first_name=None, last_name=None):
        if not email:
            raise ValueError("El usuario debe tener un correo")
        if not rut:
            raise ValueError("El usuario debe tener un rut")
        user = self.model(
            email=self.normalize_email(email),
            rut=rut,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, email, password, first_name, last_name):
        user = self.model(
            email=self.normalize_email(email),
            rut=rut,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    OP_TIPO = [
        ("1", "Estudiante"),
        ("2", "Profesor"),
        ("3", "Administrador"),
    ]
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    rut = models.CharField(max_length=12, null=False, blank=False, primary_key=True, unique=True,
                           error_messages={'unique': "Un usuario con el mismo rut ya existe."})
    email = models.EmailField(max_length=60, unique=True, null=False, blank=False,
                              error_messages={'unique': "Un usuario con el mismo correo ya existe."})
    tipo = models.CharField(max_length=30, null=True, blank=True, choices=OP_TIPO)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ["email",
                       "first_name",
                       "last_name"]

    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def get_fullname(self):
        return self.first_name + " " + self.last_name


class Asignatura(models.Model):
    codigo = models.CharField(max_length=5, null=False, blank=False, primary_key=True)
    nombreAsignatura = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.nombreAsignatura


class Profesor(Usuario):
    asignatura = models.ForeignKey(Asignatura, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Profesores"


class Alumno(Usuario):
    class Meta:
        verbose_name_plural = "Alumnos"


class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, null=True, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, null=True, on_delete=models.CASCADE)
    nota_1 = models.FloatField(blank=True, null=True)
    nota_2 = models.FloatField(blank=True, null=True)
    nota_3 = models.FloatField(blank=True, null=True)
    nota_4 = models.FloatField(blank=True, null=True)
    nota_5 = models.FloatField(blank=True, null=True)
    nota_6 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.alumno.get_fullname + " - " + self.asignatura.nombreAsignatura


class Curso(models.Model):
    nombreCurso = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    alumnos = models.ManyToManyField(Alumno, blank=True)

    def __str__(self):
        return self.nombreCurso


class Asistencia(models.Model):
    OP_ASISTIR = [
        ("Presente", "Presente"),
        ("Ausente", "Ausente"),
    ]

    alumno = models.ForeignKey(Alumno, null=True, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, null=True, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=False)
    asistencia = models.CharField(max_length=20, blank=False, null=True, choices=OP_ASISTIR)

    def __str__(self):
        return self.alumno.get_fullname + " - " + self.asignatura.nombreAsignatura + " - " + str(self.fecha)

# Asistencia str
