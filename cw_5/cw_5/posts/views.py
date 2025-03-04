from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'posts/my_posts.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html', {'post': post})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        picture = request.FILES['picture']
        thread = request.POST['thread']
        post = Post.objects.create(
            title=title,
            description=description,
            picture=picture,
            author=request.user,
            thread_id=thread
        )
        return redirect('post_list')
    return render(request, 'posts/create_post.html')

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
    return redirect('post_list')
