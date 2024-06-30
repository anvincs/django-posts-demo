from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    # order_by('-date') will order the posts by date in descending order
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})


# 'login_required' decorator checks if the user is logged in before allowing them to create a new post
# if the user is not logged in, they will be redirected to the login page given by the login_url parameter
@login_required(login_url='/users/login/')
def post_new(request):
    if request.method == 'POST':
        form = forms.createPost(request.POST, request.FILES)
        if form.is_valid():
            # save the form data to the database
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:list')
    else:     
        form = forms.createPost()
    return render(request, 'posts/post_new.html', {'form': form})