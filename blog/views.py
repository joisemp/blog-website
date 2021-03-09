from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

#def blogHome(request):
#    return render(request, 'blog_home.html', {})

class BlogHomeView(ListView):
    model = Post
    template_name = 'blog_home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'create_blog_post.html'
    fields = '__all__' # this line of code display all the fields that are defined in models.py
    # fields = ('title', 'body') # this is to choose the fields to be displayed induvidualy from models.py