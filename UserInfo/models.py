from django.db import models
from django.contrib.auth.models import User


class Info(models.Model):




    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_info")
    diet = models.TextField(blank=True)
    intolerance = models.TextField(blank=True)
    favourite1 = models.CharField(max_length=100)
    favourite2 = models.CharField(max_length=100)
    favourite3 = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.author)