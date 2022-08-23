from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Usuario



# Create your views here.


class VRegistro(LoginRequiredMixin, View):
  
    def get(self, request):
        
        form=UserCreationForm()
        return render(request,'usuarios/registro.html',{'form':form})
    
    def post(self,request):
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('inicio')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,'usuarios/registro.html',{'form':form})
        
    class Meta:
        model = Usuario