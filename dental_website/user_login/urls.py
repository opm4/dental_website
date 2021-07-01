from django.urls import path
from .views import UserRegisterView, UserEditView
# from . import views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('user_profile/', UserEditView.as_view(), name="edit_profile"),
]