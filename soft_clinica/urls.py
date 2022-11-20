"""soft_clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from .api import api
from pacientes.views import Teste2ViewSet, TesteViewSet
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'teste2', Teste2ViewSet)
router.register(r'teste', TesteViewSet)
urlpatterns = [
    path("api-rest/", include(router.urls)),
    path('api/v1/', api.urls),
    path('admin/', admin.site.urls),
    path('', include("pacientes.urls")),
    path('', include("usuarios.urls")),
    path('', include("distribuicao.urls")),
    path('', include("prontuario.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
