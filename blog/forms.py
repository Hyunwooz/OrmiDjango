from django import forms
from .models import Post

# Form
# Model Form
# 유효성 검사를 위해서 이렇게 사용함
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content']
