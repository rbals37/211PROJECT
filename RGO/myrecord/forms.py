from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        # 클래스 지정했으니 밑에 수정 금지
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'custom-title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'custom-content',
            }),
        }