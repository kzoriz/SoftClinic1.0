from django.urls import path
from django.contrib.auth import views as auth_views

from usuarios.views import signup_view, cadastro_funcionario, cadastro_docente, cadastro_discente

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="usuarios/login.html"
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', signup_view, name="signup"),

    path('cadastro-funcionario/', cadastro_funcionario, name="cadastro_funcionario"),
    path('cadastro-docente/', cadastro_docente, name="cadastro_docente"),
    path('cadastro-discente/', cadastro_discente, name="cadastro_discente"),




]