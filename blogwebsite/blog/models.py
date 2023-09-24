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
    
## Creating a new added profile user model.
class Profile(models.Model):
    ## We will associate this model with user model with onetoone association.
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    pintrest_url = models.CharField(max_length=255, null=True, blank=True)



    def __str__(self):
        return str(self.user)
    
     
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
    header_image = models.ImageField(null=True,blank=True,upload_to='images/')

    # likes = models.ManyToManyField(User,related_name = 'blog_posts')

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
    ## this method is a necessary inbuilt method which needs to be defined when using createView.

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    

# Create your models here.
