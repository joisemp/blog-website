from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Category, Post, LandingPage
from .forms import CreatePostForm, EditPostForm
from django.urls import reverse_lazy
#def blogHome(request):
#    return render(request, 'blog_home.html', {})

class LandingPageView(TemplateView):
    model = LandingPage
    template_name = 'landing_page.html'

class BlogHomeView(ListView):
    model = Post
    template_name = 'blog_home.html'
    ordering = ['-post_date','-post_time']
    # ordering = ['-id'] # This is to order the post by id but it is not efficient everytime so we can you date and time

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

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_blog_post.html'
    success_url = reverse_lazy('bloghome')

class CreateCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request, category_name):
    category_posts = Post.objects.filter(category = category_name)
    return render(request, 'categories.html', {'category_posts':category_posts, 'category_name':category_name.title()})