from django.urls import path 
from . import views

urlpatterns = [
    # path("",views.start)
    path("login",views.login),
    path("register",views.register),
    path("logout",views.logout)
]