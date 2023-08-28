from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
## For our special editor.

## New model for category.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # body = models.TextField() 
    ## We are going to be using a rich text editor for this insteda of normal text field.

    body = RichTextField(blank=True, null=True)

    post_date = models.DateTimeField(auto_now=True) ## Whenever we create new blogposts, automatically assign a date to it.
    category = models.CharField(max_length=255,default='uncategorised')

    snippet = models.CharField(max_length=255,default='Click link above to read the blogpost.')

    # likes = models.ManyToManyField(User,related_name = 'blog_posts')

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
    ## this method is a necessary inbuilt method which needs to be defined when using createView.

    

# Create your models here.
