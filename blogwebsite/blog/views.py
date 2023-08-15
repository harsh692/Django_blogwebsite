from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView ## class based views
## Using class views is helping us.
from .models import Post
from .forms import ArticalPostForm


# def home(request):
#     return render(request,'home.html',{})

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html' 

class ArticalDetailView(DetailView):
    model = Post
    template_name = 'articalDetails.html'

class PostView(CreateView):
    model = Post
    template_name = 'post.html'
    form_class = ArticalPostForm
    # fields = '__all__'