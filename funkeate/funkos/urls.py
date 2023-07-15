from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from . import views

app_name = "funkos"

router = routers.DefaultRouter()
router.register(r'products', views.FunkosProductoViewSet)
router.register(r'categories', views.FunkosCategoriaViewSet)
router.register(r'users', views.FunkosUsuariosViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.HomeView.as_view(), name ='home'),
    path('token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
    path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]