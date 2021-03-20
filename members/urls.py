from re import template
from django import views
from django.urls import path
from .views import ProfilePageView, UserEditView, UserRegisterView, PasswordsChangeView, EditProfilePageView
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name= 'register'),
    path('edit_profile/', UserEditView.as_view(), name= 'edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
]
