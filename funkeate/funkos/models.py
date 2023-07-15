from django.db import models

# Create your models here.

class FunkosCategoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default = True, blank=True, null=True)
    nombre = models.CharField(unique=True, max_length=55)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'funkos_categoria'

    def __str__(self):
        return self.nombre


class FunkosProducto(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField(default = True, blank=True, null=True)
    imagen = models.CharField(unique=True, max_length=255)
    nombre = models.CharField(unique=True, max_length=55)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    update_at = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(FunkosCategoria, on_delete=models.CASCADE)
    caja_personalizada = models.BooleanField(default=True)
    detalles = models.CharField(max_length=255, blank=True, null=True)
    personalizable = models.BooleanField(default=True)
    tamaño_caja =  models.CharField(max_length=50, default='16x12x9 cm')
    tamaño_funko = models.CharField(max_length=50, default='13x6 cm')

    class Meta:
        managed = False
        db_table = 'funkos_producto'

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(max_length=255, null=False, unique= True)
    email_verified = models.BooleanField(default=False ,blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_staff = models.BooleanField(default=False, blank=True, null=True)
    is_superuser = models.BooleanField(default=False, blank=True, null=True)
    last_login = models.DateTimeField(auto_now=True)
    nickname = models.CharField(unique=True, max_length=255)
    password = models.CharField(unique=True, max_length=124)
    username = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'users'