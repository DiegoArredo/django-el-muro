from django.db import models
from account.models import User

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=280)
    user = models.ForeignKey(User,related_name="messages",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #comments 


class Comment(models.Model):
    comment = models.CharField(max_length=280)
    message = models.ForeignKey(Message,related_name="comments",on_delete=models.CASCADE)
    user= models.ForeignKey(User,related_name="my_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)