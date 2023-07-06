from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # on_delete는 참조하는 post가 지워질 경우 같이 삭제한다는 옵션
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment on {self.post.title}'


class HashTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name