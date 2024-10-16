"""
URL configuration for ApiBancaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Banco Django Brasil",
      default_version='v1',
      description="Documentação da API com Swagger",
      terms_of_service="#",
      contact=openapi.Contact(email="contato@seusite.com"),
      license=openapi.License(name="Licença BSD"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin do Django
    path('admin/', admin.site.urls),
    
    # URLs da API com prefixo "api/v1/"
    path('api/v1/', include([
        path('cliente/', include('apps.clientes.urls')),
        path('emprestimos/', include('apps.emprestimos.urls')),
        path('produtos/', include('apps.produtos.urls')),
        
        # URLs para a documentação Swagger e ReDoc
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ])),
]
