from django.urls import path
#from . import views
from.views import BlogHomeView, BlogDetailView, CreatePostView, UpdatePostView, DeletePostView, LandingPageView
urlpatterns = [
    #path('', views.blogHome, name="blogHome"),
    path('', LandingPageView.as_view(), name='landingpage'),
    path('blog/', BlogHomeView.as_view(), name='bloghome'),
    path('article/<int:pk>', BlogDetailView.as_view(), name='blogdetail'),
    path('createPost/', CreatePostView.as_view(), name='createPost'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='updatePost'),
    path('article/<int:pk>/remove/', DeletePostView.as_view(), name='deletePost'),
]