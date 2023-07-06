from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Comment, HashTag


### post
class Index(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialized_posts = PostSerializer(posts) # 직렬화
        return Response(serialized_posts.data)