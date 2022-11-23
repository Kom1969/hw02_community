from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Group
from django.shortcuts import render, get_object_or_404

# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 


# Страница с информацией об публикациях;
# view-функция принимает параметр slug из path()
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_posts.html', context) 