from django import forms
from .models import Post, Category

## Hard coding categories
# choices = [('sports','sports'),('entertainment','entertainment'),('coding','coding')]

## Soft coding categories
choices = Category.objects.all().values_list('name','name')
## This is actually a queryset, we need a list of tuples.
choice_list=[]
for c in choices:
    choice_list.append(c)



class ArticalPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Title of the article'}),
            'title_tag'  : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Sub-title'}),
            # 'author'  : forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Select author'}),
            'author'  : forms.TextInput(attrs={'class': 'form-control', 'id':'author_id', 'value':'user name','type':'hidden'}),
            'category' : forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body'  : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Main content'}),
            }
        

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','category')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Title of the article'}),
            'title_tag'  : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Sub-title'}),
            # 'author'  : forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Select author'}),
            'body'  : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Main content'}),
            'category' : forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            }
        
