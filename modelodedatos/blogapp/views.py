from django.shortcuts import render
from .models import Post

def mostrar_posts(request):
    posts = Post.objects.all()
    return render(request, 'home_blog.html', {'posts':posts})
