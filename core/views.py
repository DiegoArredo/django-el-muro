from django.shortcuts import redirect, render
from django.contrib import messages
from core.models import Message,Comment,User

# Create your views here.

def test(request): 
    return render(request, "core/base.html")

def index(request):
    if "usuario" in request.session:
        context ={
            "mensajes" : Message.objects.all().order_by("-created_at")
        }

        return render(request, "core/muro.html",context)

    else:
        return redirect("/account/login")

def post_message(request):
    if request.method == "POST":
        print(request.POST)
        user_m = User.objects.get(id=request.session["usuario"]["id"])
        new_message = Message.objects.create(
            message = request.POST["message"],
            user = user_m
        )
        messages.info(request,"Se ha publicado tu mensaje!")
        return redirect("/")

def post_comment(request):
    if request.method == "POST":
        message_c = Message.objects.get(id=request.POST["message_id"])
        user_c = User.objects.get(id=request.session["usuario"]["id"])
        new_comment = Comment.objects.create(
            comment = request.POST["comment"],
            message = message_c,
            user = user_c
        )
        messages.info(request,"Se ha publicado el comentario!")
        return redirect("/")

def delete_message(request):
    if request.method == "POST":
        message_d = Message.objects.get(id=request.POST["message_id"])
        message_d.delete()
        messages.error(request, "Se ha eliminado el mensaje correctamente")
        return redirect("/")