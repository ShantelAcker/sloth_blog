from django.shortcuts import render

from .models import Post

# Create your views here.


def index(request):
    """The home page of the blog that lists all posts."""
    posts = Post.objects.order_by('pub_date')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def about(request):
    """A page detailing information about myself."""
    return render(request, 'blog/about.html')
