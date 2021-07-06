import os
from django.apps import AppConfig

if os.name == 'nt':
        name_var = 'blog'
else:
        name_var = 'dental_website.blog'

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
