from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('blogdetail', args=(str(self.id)) # to return to the post created in detailview after clicking on post button
        return reverse('bloghome') # to return to the blog home page after clicking on post button


class Post(models.Model): 
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='others')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/thubnail')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title+' | '+str(self.author)

    def get_absolute_url(self):
        #return reverse('blogdetail', args=(str(self.id)) # to return to the post created in detailview after clicking on post button
        return reverse('bloghome') # to return to the blog home page after clicking on post button


class LandingPage(models.Model): 
    title = models.CharField(max_length=255)
    body = models.TextField()

# to delete the image while deleting the post

@receiver(pre_delete, sender=Post)
def Post_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.thumbnail.delete(False)