from django.shortcuts import render
from django.core.mail import send_mail
from .models import Service

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def pricing(request):
    services = Service.objects.all()
    return render(request, 'pricing.html', {'services':services})

def service(request):
    return render(request, 'service.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blog_details(request):
    return render(request, 'blog-details.html', {})

def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']
        
        # Send an email
        appointment_msg = f"""Name: {your_name}
Phone: {your_phone}
Address: {your_address}
Schedule: {your_schedule}
Date: {your_date}
Message: {your_message}"""
        
        send_mail(
            'Appointment Request ' + your_name, # Subject
            appointment_msg, # Message 
            your_email, # From E-mail
            ['send.mail.test.871@gmail.com'], # To Email
        )
        
        return render(request, 'appointment.html', {
            
            'your_name' : your_name,
            'your_phone' : your_phone,
            'your_email' : your_email,
            'your_address' : your_address,
            'your_schedule' : your_schedule, 
            'your_date' : your_date,
            'your_message' : your_message
            
            })
    else:
        return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        # Send an email
        send_mail(
            'Contact form from ' + message_name, # Subject
            message + '\n Mail: ' + message_email, # Message 
            message_email, # From E-mail
            ['send.mail.test.871@gmail.com'], # To Email
        )

        return render(request, 'contact.html', {'message_name' : message_name})
    else:
        return render(request, 'contact.html', {})
    
def newsletter(request):
    if request.method == "POST":
        nl_email = request.POST['nl-email']
        
        # Send an email
        send_mail(
            'Newsletter request from ' + nl_email, # Subject
            'Please subscribe the following addres to Newsletter:' + '\n Mail: ' + nl_email, # Message 
            nl_email, # From E-mail
            ['send.mail.test.871@gmail.com'], # To Email
        )

        return render(request, 'newsletter.html', {'nl_email' : nl_email})
    else:
        return render(request, 'home.html', {})