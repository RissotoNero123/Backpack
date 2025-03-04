from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    picture = models.FileField(upload_to='images/')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
