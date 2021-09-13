from django.urls import path 
from . import  views

urlpatterns = [
    # path("",views.test)
    path("",views.index),
    path("message/post",views.post_message),
    path("message/comment/post",views.post_comment),
    path("message/delete",views.delete_message)
]
