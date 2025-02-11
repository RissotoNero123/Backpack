from django.db import models
import os
# Create your models here.

class Movie(models.Model): 
    title = models.CharField('Название',max_length=50)
    description = models.CharField('Описание',max_length=250)
    producer = models.CharField('Продюсер',max_length=50)
    duration = models.IntegerField('Проделжительность')
    
    def __str__(self):
        return self.title
     
class Article(models.Model): 
    title = models.CharField('Название',max_length=50)
    text = models.CharField('Текст',max_length=250)
    author = models.CharField('Автор',max_length=50)
    
    def __str__(self):
        return self.title
    