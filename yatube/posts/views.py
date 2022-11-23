from django.shortcuts import render
from .models import Post, Group
from django.shortcuts import get_object_or_404


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
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
