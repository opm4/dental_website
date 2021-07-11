# import os
from django.apps import AppConfig

# if os.name == 'nt':
#         name_var = 'website'
# else:
#         name_var = 'dental_website.website'

class WebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website'
