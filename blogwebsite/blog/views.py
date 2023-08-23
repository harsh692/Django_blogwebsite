from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView ## class based views
## Using class views is helping us.
from .models import Post, Category
from .forms import ArticalPostForm, EditPostForm
from django.urls import reverse_lazy


## CLASS BASED VIEWS

class HomeView(ListView):
    model = Post
    template_name = 'home.html' 
    # ordering =['-id']
    ## id is created automatically but we want it to be descending id list therefore ordering by -ve.
    ordering = ['-post_date'] ## post_date is the field in model.

    ## In order to pass a different variable or object to the class based view, we need to write some code.
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context
    


class ArticalDetailView(DetailView):
    model = Post
    template_name = 'articalDetails.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticalDetailView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context

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
    

## FUNCTION BASED VIEWS
    
# def home(request):
#     return render(request,'home.html',{})

## In our class based view database queries are done by themselves, here we have to do it by ourselves.

def CategoryViewTwo(request,cats):
    category_posts = Post.objects.filter(category = cats.replace('-',' '))
    return render(request,'categoryContent.html',{'category_posts':category_posts, 'cats':cats.replace('-',' ')})

def CategoryPageView(request):
    categories = Category.objects.all()
    return render(request,'categoryPage.html',{'categories':categories})
