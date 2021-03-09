from django.urls import path
#from . import views
from.views import BlogHomeView, BlogDetailView

urlpatterns = [
    #path('', views.blogHome, name="blogHome"),
    path('', BlogHomeView.as_view(), name='bloghome'),
    path('article/<int:pk>', BlogDetailView.as_view(), name='blogdetail')
]