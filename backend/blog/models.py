from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)