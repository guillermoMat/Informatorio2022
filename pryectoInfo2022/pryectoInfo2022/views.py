# from http.client import HTTPResponse
from django.shortcuts import render


def inicio(request):
    return render(request,'inicio.html')

def campañas(request):
    return render(request,'campanias.html')