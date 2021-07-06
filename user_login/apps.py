import os
from django.apps import AppConfig

if os.name == 'nt':
        name_var = 'user_login'
else:
        name_var = 'dental_website.user_login'

class UserLoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = name_var
