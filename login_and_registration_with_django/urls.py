"""
URL configuration for login_and_registration_with_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView
from core import views
# from .views import CustomPasswordChangeView  # Importe a nova visualização personalizada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('password_change/', views.CustomPasswordChangeView.as_view(
        template_name='registration/custom_password_change_form.html',
    ), name='password_change'),  # Use a visualização personalizada
    path('password_change/password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('list_users/', views.list_users, name='list_users'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user')
]
