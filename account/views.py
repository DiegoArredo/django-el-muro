from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.

def logout(request): 
    if "usuario" in request.session:
        del request.session["usuario"]
        messages.info(request,"Vuelve pronto!")
    return redirect("/account/login")

def login(request):
    if request.method == "GET":
        if "usuario" in request.session:
            messages.info(request,"Ya estas logueado!!")
            return redirect("/")
        return render(request,"account/login.html")


    if request.method == "POST":
        usuario = User.objects.filter(email = request.POST["email"].lower())
        if usuario:
            logged_user = usuario[0]
        else:
            messages.warning(request,"El email no se encuentra registrado!")
            return redirect("/account/login")

        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):

            request.session["usuario"] = {
                "id" : logged_user.id,
                "nombre" : f"{logged_user.nombre} {logged_user.apellido}",
                "email" : logged_user.email,
                ############################################
                "fecha_nacimiento" : str(logged_user.fecha_nacimiento) ############################################
            }
            messages.success(request,"Logueado correctamente! :D")
            return redirect("/")
        else:
            messages.error(request,"Contraseña incorrecta!")
        return redirect("/account/login")


def register(request):
    if request.method == "GET":
        if "usuario" in request.session:
            messages.info(request,"Para registrar una cuenta debes salir de la actual!")
            return redirect("/")
        else:
            return render(request,"account/register.html")


    if request.method == "POST":
        print(request.POST)

        errors = User.objects.validator(request.POST)
        print(errors)
        if len(errors) > 0 :
            
            for key, value in errors.items():

                messages.error(request,value)

            return redirect("/account/register")   

        else:
            new_user = User.objects.create(
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                email = request.POST["email"].lower(),
                fecha_nacimiento = request.POST["fecha_nacimiento"],
                password = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
            )
            print("SE HA CREADO LA CUENTA")
            messages.success(request, "Te has registrado correctamente!")
            return redirect("/account/login")
        




