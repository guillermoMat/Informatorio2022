from django.shortcuts import render

# Create your views here.
def inicio(request):
    nombre = "Nestor Acevedo"
    lista = ["Acevedo","Alegre","Alvarin","Alvarez","Busi","Echavarria","Mathieu","Salcedo","Sotelo"]
    return render(request,'inicio.html', {"nom":nombre,"lis":lista})
    
   

    