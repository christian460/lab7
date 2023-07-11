from django.conf import settings 
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def enviar(request):
    send_mail('Aria: '+request.POST['lselect'],
    'Hola '+request.POST['lname']+', te hablamos de Aria te agredecemos que estes interesados en nuestro proyecto. En breve te contactaremos al numero '
    +request.POST['lphone'],
    settings.EMAIL_HOST_USER,
    [request.POST['lemail']],
    fail_silently=False)
    
    return render(request,'enviar.html')