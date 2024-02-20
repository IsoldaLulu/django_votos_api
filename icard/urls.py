from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#importaciones de rutas creadas en nuestro proyecto
from users.api.router import router_user
from rango.api.router import router_rango

schema_view = get_schema_view(
   openapi.Info(
      title="iCard_ApiDoc",
      default_version='v1',
      description="documentacion de la api icard",
      terms_of_service="https://pfr2102.github.io/PORTAFOLIO/",
      contact=openapi.Contact(email="pfrs2102@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    #rutas globales de django
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #rutas de nuestras api
    path('api/', include(router_user.urls)),
    path('api/', include('users.api.router')),#esta ruta es diferente porque es para saber los datos del usuario que se autentica
    path('api/', include(router_rango.urls)),
]
