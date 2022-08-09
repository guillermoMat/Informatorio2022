# from http.client import HTTPResponse
from django.shortcuts import render


def inicio(request):
    return render(request,'inicio.html')