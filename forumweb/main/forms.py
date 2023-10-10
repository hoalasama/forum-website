from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget
from .models import Category

class PostForm(forms.ModelForm):
    #Post.content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ["title", "content", "categories", "tags", "image"]
        widgets = {
            'content': CKEditorWidget()
        }
class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "categories", "tags", "image"]
        widgets = {
            'content': CKEditorWidget()
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']