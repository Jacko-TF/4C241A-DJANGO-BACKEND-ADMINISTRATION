from django.contrib import admin

from .models import FunkosCategoria, FunkosProducto, Users

# Register your models here.

class FunkosCategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','created_at','estado','nombre','imagen','update_at']

class FunkosProductoAdmin(admin.ModelAdmin):
    list_display = ['id','created_at','descripcion','estado','imagen','nombre','precio','caja_personalizada','detalles','personalizable','tamaño_caja','tamaño_funko','update_at','categoria']

class UsersAdmin(admin.ModelAdmin):
    list_display = ['id','created_at','date_joined','email','email_verified','is_active','is_staff','is_superuser','last_login','nickname','password', 'username']

admin.site.register(FunkosCategoria,FunkosCategoriaAdmin)
admin.site.register(FunkosProducto,FunkosProductoAdmin)
admin.site.register(Users,UsersAdmin)

