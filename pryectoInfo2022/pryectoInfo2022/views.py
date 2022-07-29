from http.client import HTTPResponse
from django.shortcuts import render


def inicio(request):
    nombre = "Nestor Acevedo"
    lista = ["Acevedo","Alegre","Alvarin","Alvarez","Busi","Echavarria","Mathieu","Salcedo","Sotelo"]
    return render(request,'inicio.html', {"nom":nombre,"lis":lista})
    
   

    