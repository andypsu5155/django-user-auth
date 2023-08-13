from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login_user", views.login_user, name='login-user'),
    path("logout_user", views.logout_user, name='logout-user'),
    path("register", views.register, name='register'),
    path("error_login", views.error_login, name="error_login"),
]
