from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def login(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
            
        user = authenticate( correo = correo, contrasena = contraseña )
        if user:
            login(request, user)
            messages.success(request,'Bienvenido {}'.format(correo,correo))

            return redirect('home')
        else:
            messages.error(request, 'Correo o Contraseña incorrectas')    


    return render(request,'app/registration/login.html')

def registro(request):
    return render(request,'app/registro.html')

def page1(request):
    return render(request,'app/page1.html')

def adminT(request):
    return render(request,'app/adminT.html')

def adminU(request):
    return render(request,'app/adminU.html')

def crearUsuario(request):
    return render(request,'app/crearUsuario.html')

def crearTrivia(request):
    return render(request,'app/crearTrivia.html')

def partida(request):
    return render(request,'app/partida.html')

def ruleta(request):
    return render(request,'app/ruleta.html')

def partida(request):
    return render(request,'app/partida.html')

