from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
from .forms import FormContacto

def contacto(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        miFormulario = FormContacto(request.POST)
        # check whether it's valid:
        if miFormulario.is_valid():
            # process the data in form.cleaned_data as required
            infoFormulario = miFormulario.cleaned_data
            send_mail(infoFormulario['asunto'],infoFormulario['mensaje'],infoFormulario.get('email',''),['nesky66@gmail.com'],)
            
            # redirect to a new URL:
            return render(request,'thanks.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        miFormulario = FormContacto()

    return render(request, 'contacto.html', {'form': miFormulario})