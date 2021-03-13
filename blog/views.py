from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CreatePostForm, EditPostForm
from django.urls import reverse_lazy
#def blogHome(request):
#    return render(request, 'blog_home.html', {})

class BlogHomeView(ListView):
    model = Post
    template_name = 'Blog/blog_home.html'
    ordering = ['-post_date','-post_time']
    # ordering = ['-id'] # This is to order the post by id but it is not efficient everytime so we can you date and time

class BlogDetailView(DetailView):
    model = Post
    template_name = 'Blog/blog_detail.html'

class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm # we imported the form from forms.py file so using this instead of field because we not need those
    template_name = 'Blog/create_blog_post.html'
    # fields = '__all__' # this line of code display all the fields that are defined in models.py
    # fields = ('title', 'body') # this is to choose the fields to be displayed induvidualy from models.py

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'Blog/update_blog_post.html'
    # fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'Blog/delete_blog_post.html'
    success_url = reverse_lazy('bloghome')