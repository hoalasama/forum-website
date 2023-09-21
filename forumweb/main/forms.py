from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

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
        