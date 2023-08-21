from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView ## class based views
## Using class views is helping us.
from .models import Post, Category
from .forms import ArticalPostForm, EditPostForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request,'home.html',{})

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html' 
    # ordering =['-id']
    # id is created automatically but we want it to be descending id list therefore ordering by -ve.
    ordering = ['-post_date'] ## post_date is the field in model.
    


class ArticalDetailView(DetailView):
    model = Post
    template_name = 'articalDetails.html'

class PostView(CreateView):
    model = Post
    template_name = 'post.html'
    form_class = ArticalPostForm
    # fields = '__all__'

class Update_View(UpdateView):
    model = Post
    template_name = 'update_post.html'
    # fields = ['title','title_tag','body']
    form_class = EditPostForm

class Delete_View(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class Category_View(CreateView):
    model = Category
    template_name = 'category.html'
    fields = '__all__'
    