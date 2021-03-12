from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import CreatePostForm, EditPostForm

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
    form_class = CreatePostForm # we imported the form from forms.py file so using this instead of field because we not need those
    template_name = 'create_blog_post.html'
    # fields = '__all__' # this line of code display all the fields that are defined in models.py
    # fields = ('title', 'body') # this is to choose the fields to be displayed induvidualy from models.py

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update_blog_post.html'
    # fields = ['title', 'body']