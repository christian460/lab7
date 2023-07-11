from django.conf import settings 
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def enviar(request):
    send_mail('Un email desde django', 
    'Hola te escribimos desde django',
    settings.EMAIL_HOST_USER,
    ['juego4661@gmail.com'],
    fail_silently=False)
    
    return render(request,'enviar.html')