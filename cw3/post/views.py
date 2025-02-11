from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def redirect_to_threads(request):
    return redirect('thread_list')

def thread_list(request):
    threads = Thread.objects.all()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm()
    return render(request, 'post/thread_list.html', {'threads': threads, 'form': form})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = thread.posts.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=id)
    else:
        form = PostForm()
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})