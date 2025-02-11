from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'mainBlog.html', {'articles': articles})

def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'BlogDetail.html', {'article': article})