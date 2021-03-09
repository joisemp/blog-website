from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

#def blogHome(request):
#    return render(request, 'blog_home.html', {})

class BlogHomeView(ListView):
    model = Post
    template_name = 'blog_home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'