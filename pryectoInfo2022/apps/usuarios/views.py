from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class VRegistro(LoginRequiredMixin, View):
    
    def get(self, request):
        
        form=UserCreationForm()
        return render(request,'usuarios/registro.html',{'form':form})
    
    def post(self,request):
        pass