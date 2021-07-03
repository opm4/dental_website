from django import views
from django.urls import path
from .views import ShowProfilePageView, UserRegisterView, UserEditView, PasswordsChangeView, password_success
from django.contrib.auth import views as auth_views
# from . import views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('user_profile/', UserEditView.as_view(), name="edit_profile"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name="edit_password"),
    path('password/', PasswordsChangeView.as_view(), name="edit_password"),
    path('password_success/', password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="show_profile_page")
]