from django.shortcuts import render
from .models import Post, Group
from django.shortcuts import get_object_or_404


def index(request):
    quantity_posts=10 #Количество элементов списка 
    posts = Post.objects.order_by('-pub_date')[:quantity_posts]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


""" 
Страница с информацией об публикациях;
view-функция принимает параметр slug из path()
"""
def group_posts(request, slug):
    quantity_posts=10 #Количество элементов списка
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:quantity_posts]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
