from blog.models import Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Category, Post, LandingPage
from .forms import CreatePostForm, EditPostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
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

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(BlogHomeView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        likes_count = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = likes_count.total_likes()

        liked = False
        if likes_count.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

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

def CategoryListView(request):
    category_menu_list = Category.objects.all()
    return render(request, 'categories_list.html', {'category_menu_list': category_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blogdetail', args=[str(pk)]))
