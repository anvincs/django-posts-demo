from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    # order_by('-date') will order the posts by date in descending order
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})