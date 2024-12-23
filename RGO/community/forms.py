from django import forms
from .models import Post

#폼 생성
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content'] 