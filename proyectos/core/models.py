from django.db import models

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Categoria')
#     description = models.TextField(verbose_name='Descripción')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'categoria'
#         verbose_name_plural = 'categorias'
#         db_table = 'categoria'
#         ordering = ['id']

# class Product(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Nombre')
#     price = models.FloatField(verbose_name='Precio')
#     description = models.TextField(verbose_name='Descripción')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE) asi se agrega im fk

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Producto'
#         verbose_name_plural = 'Productos'
#         db_table = 'producto'
#         ordering = ['id']
#1 ---------tabla-fuerte-------------------------------------------------------------------------------------------
class Curso(models.Model):
    # id_curso = models.IntegerField(verbose_name='id del curso')
    codigo_curso = models.CharField(max_length=5,verbose_name='Codigo del curso')
    nombre_curso = models.CharField(max_length=5,verbose_name='Nombre del curso')

    def __str__(self):
        return self.codigo_curso

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        db_table = 'curso'
        ordering = ['id']
#2 ---------tabla-fuerte-------------------------------------------------------------------------------------------
class Categoria_herramienta(models.Model):
    # id_est_her = models.IntegerField(verbose_name='id del curso')
    nombre = models.CharField(max_length=25, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria herramienta'
        verbose_name_plural = 'Categoria herramientas'
        db_table = 'categoria_herramienta'
        ordering = ['id']
#3 ----tabla-fuerte------------------------------------------------------------------------------------------------
class Rol(models.Model):
    # id_rol = models.IntegerField(verbose_name='id del rol')
    nombre = models.CharField(max_length=45,verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion del rol')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table = 'rol'
        ordering = ['id']
#4 ----tabla-fuerte-----------------------------------------------------------------------------------------------
class Wiki(models.Model):
    # id_wiki = models.IntegerField(verbose_name='id de la wiki')
    nombre = models.CharField(max_length=150,verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion')
    referencias_web = models.TextField(verbose_name='Referencias web')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Wiki'
        verbose_name_plural = 'Wikis'
        db_table = 'wiki'
        ordering = ['id']
#5 --------tabla-fuerte------------------------------------------------------------------------------------------
class Zona(models.Model):
    # id_rol = models.IntegerField(verbose_name='id de la zona')
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion de la zona')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'
        db_table = 'zona'
        ordering = ['id']
#6 ------tabla-debil----------------------------------------------------------------------------------------------
class Herramienta(models.Model):
    # id_inv_her = models.IntegerField(verbose_name='id del inventario de la herramieta'
    nombre = models.CharField(max_length=25, verbose_name='Nombre')
    class Disponibilidad(models.TextChoices):
        DISPONIBLE = "disponible"
        NODISPONIBLE = "no disponible"
    disponibilidad = models.CharField(choices=Disponibilidad.choices,max_length=15, verbose_name='Disponibilidad')
    Estado_herramienta = models.ForeignKey(Categoria_herramienta, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Herramienta'
        verbose_name_plural = 'Herramientas'
        db_table = 'herramienta'
        ordering = ['id']
#7 --------tabla-debil--------------------------------------------------------------------------------------------
class Asistencia(models.Model):
    # id_asistencia = models.IntegerField(verbose_name='Asistencia')
    class Estado(models.TextChoices):
        BUENO = "asistio"
        REGULAR = "no asistio"
    estado = models.CharField(choices=Estado.choices,max_length=20, verbose_name='Estado')
    fecha_asistencia = models.DateField(verbose_name='Fecha_asistencia')
    horas = models.IntegerField(verbose_name='Horas')
    # id_usuario = models.IntegerField(verbose_name='Usuario')
    # Users = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        db_table = 'asistencia'
        ordering = ['id']
#8 ------tabla-debil----------------------------------------------------------------------------------------------
class Labor_social(models.Model):
    # id_labor_social = models.IntegerField(verbose_name='id de la labor social')
    nombre = models.CharField(max_length=150,verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion')
    # id_wiki = models.IntegerField(verbose_name='Wiki')
    Wiki = models.ForeignKey(Wiki, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Labor social'
        verbose_name_plural = 'Labores sociales'
        db_table = 'labor_social'
        ordering = ['id']
#9 ----------tabla-debil------------------------------------------------------------------------------------------
class Cronograma_actividad(models.Model):
    # id_cro_act = models.IntegerField(verbose_name='Cronograma')
    fecha_inicio = models.DateField(verbose_name='Fecha_inicio')
    fecha_fin = models.DateField(verbose_name='Fecha_fin')
    # id_labor_social = models.IntegerField(verbose_name='Actividad')
    # id_zona = models.IntegerField(verbose_name='Zona')
    Labor_social = models.ForeignKey(Labor_social, on_delete=models.CASCADE)
    Zona = models.ForeignKey(Zona, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha_inicio

    class Meta:
        verbose_name = 'Cronograma actividad'
        verbose_name_plural = 'Cronograma actividades'
        db_table = 'cronograma_actividad'
        ordering = ['id']
#10 --------tabla-debil--------------------------------------------------------------------------------------------
class Prestamo(models.Model):
    # id_usuario = models.IntegerField(verbose_name='Id del usuario')
    # id_his_her = models.IntegerField(verbose_name='Id de el historico')
    # fecha_entrega = models.DateField(verbose_name='Fecha entrega')
    # fecha_devolucion = models.DateField(verbose_name='Fecha devolucion')
    class Estado(models.TextChoices):
        ACTIVO = "activo"
        INACTIVO = "inactivo"

    estado = models.CharField(choices=Estado.choices,max_length=20, verbose_name='Estado')
    descripcion = models.TextField(verbose_name='Descripcion')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    # id_inv_her = models.IntegerField(verbose_name='Id del inventario de la herramienta')

    herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE)
    # Users = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha_entrega

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        db_table = 'prestamo'
        ordering = ['id']
#11 ----------------------------------------------------------------------------------------------------
# class Usuario(models.Model):
#     id_usuario = models.IntegerField(verbose_name='id del usuario')
#     nombres = models.CharField(max_length=25, verbose_name='Nombres')
#     apellidos = models.CharField(max_length=25, verbose_name='Apellidos')
#     documento = models.IntegerField(verbose_name='Documento')
#     class Jornada(models.IntegerChoices):
#         MAÑANA = 1 #"mañana"
#         TARDE = 2 #"tarde"
#     jornada = models.IntegerField(choices=Jornada.choices, verbose_name='Jornada')
#     contrasena = models.CharField(max_length=100, verbose_name='Contraseña')
#     class Estado(models.IntegerChoices):
#         ACTIVO = 1 #"activo"
#         INACTIVO = 2 #"inactivo"
#     estado = models.IntegerField(choices=Estado.choices, verbose_name='Estado')
#     id_rol = models.IntegerField('id del rol')
#     id_curso = models.IntegerField(verbose_name='id del curso')
#     id_cro_act = models.IntegerField(verbose_name='id del cronograma de actividades')

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = 'usuario'
#         verbose_name_plural = 'usuarios'
#         db_table = 'usuario'
#         ordering = ['id']
