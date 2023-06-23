from django import forms
from .models import Post, Comment, HashTag

# Form: html에 있는 form 태그
# Model Form: model을 사용하는 form
# 유효성 검사를 위해서 이렇게 사용함
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content']
        

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': '50','rows': '2'})
        }


class HashTagForm(forms.ModelForm):
    
    class Meta:
        model = HashTag
        fields = ['name']
