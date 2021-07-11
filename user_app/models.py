from typing import Text
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post_Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)