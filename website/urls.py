from django.urls import path
from .views import home, contact, about, pricing, service, \
    blog, blog_details, appointment, newsletter

urlpatterns = [
    path('', home, name="home"),
    path('contact.html', contact, name="contact"),
    path('about.html', about, name="about"),
    path('pricing.html', pricing, name="pricing"),
    path('service.html', service, name="service"),
    path('blog.html', blog, name="blog"),
    path('blog-details.html', blog_details, name="blog_details"),
    path('appointment.html', appointment, name="appointment"),
    path('newsletter.html', newsletter, name="newsletter"),
]