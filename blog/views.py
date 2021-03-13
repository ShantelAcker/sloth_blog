from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.


def index(request):
    """The home page of the blog that lists all posts."""
    posts = Post.objects.order_by('-pub_date')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def post(request, post_id):
    """Show a single post and all its content."""
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blog/post.html', context)


def about(request):
    """A page detailing information about myself."""
    return render(request, 'blog/about.html')
