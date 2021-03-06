"""dental_website URL Configuration

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
# import os
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static 

# if os.name == 'nt':
#     website_url = 'website.urls'
#     blog_url = 'blog.urls'
#     login_url = 'user_login.urls'
# else:
#     website_url = 'dental_website.website.urls'
#     blog_url = 'dental_website.blog.urls'
#     login_url = 'dental_website.user_login.urls'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('blog/', include('blog.urls')),
    path('user_login/', include('django.contrib.auth.urls')),
    path('user_login/', include('user_login.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
