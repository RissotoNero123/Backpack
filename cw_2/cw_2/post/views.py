# post/views.py
from django.shortcuts import render, redirect
from .forms import PostForm
from django.views import View

class PostCreateView(View):
    def get(self, request):
        form = PostForm()  # создаем пустую форму
        return render(request, 'post/post_form.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)  # передаем данные из формы
        if form.is_valid():  # проверяем, что данные формы валидны
            form.save()  # сохраняем новый объект Post в базу данных
            return redirect('post-list')  # перенаправляем на список постов (можно изменить)
        return render(request, 'post/post_form.html', {'form': form})  # если форма невалидна, показываем ее заново
