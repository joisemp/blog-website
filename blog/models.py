from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model): 
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField() 

    def __str__(self):
        return self.title+' | '+str(self.author)

    def get_absolute_url(self):
        #return reverse('blogdetail', args=(str(self.id)) # to return to the post created in detailview after clicking on post button
        return reverse('bloghome') # to return to the blog home page after clicking on post button
