from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Thread, Post

admin.site.register(Thread)
admin.site.register(Post)