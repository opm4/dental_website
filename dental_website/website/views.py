from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def service(request):
    return render(request, 'service.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blog_details(request):
    return render(request, 'blog-details.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        # Send an email
        send_mail(
            'Contact form from ' + message_name, # Subject
            message, # Message 
            message_email, # From E-mail
            ['office_business@provider.com'], # To Email
        )

        return render(request, 'contact.html', {'message_name' : message_name})
    else:
        return render(request, 'contact.html', {})