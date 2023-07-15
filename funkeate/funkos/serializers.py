from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import Users, FunkosProducto, FunkosCategoria
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

#APLICACION FUNKEATE
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="funkos:funkoscategoria-detail")
    class Meta:
        model = FunkosCategoria
        fields = ['url','id','nombre','estado','created_at','update_at']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categoria = CategorySerializer()
    url = serializers.HyperlinkedIdentityField(view_name="funkos:funkosproducto-detail")
    class Meta:
        model = FunkosProducto
        fields = ['url','id','nombre','estado','imagen','descripcion','detalles','precio','caja_personalizada','personalizable','tamaño_caja','tamaño_funko','categoria','created_at','update_at']

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="funkos:users-detail")
    class Meta:
        model = Users
        fields = ['url','id','username','nickname','password','email','email_verified','is_active','is_staff','is_superuser','created_at','date_joined']