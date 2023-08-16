from django import forms
from .models import Post

class ArticalPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Title of the article'}),
            'title_tag'  : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Sub-title'}),
            'author'  : forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Select author'}),
            'body'  : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Main content'}),
            }
        

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Title of the article'}),
            'title_tag'  : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Sub-title'}),
            # 'author'  : forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Select author'}),
            'body'  : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Main content'}),
            }