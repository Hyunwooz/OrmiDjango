from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer, CommentSerializer, HashtagSerializer


### post
class Index(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialized_posts = PostSerializer(posts, many=True) # 직렬화
        return Response(serialized_posts.data)
# Y1HFbRb274izMkDBkGeVRBxir6QXolTw

class Write(APIView):
    def post(self, request):
        
        serializer = PostSerializer(data=request.POST)
        
        if serializer.is_valid():
            
            post = serializer.save(commit=False)
            post.writer = request.user
            post.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

### Comment
class CommentWrite(APIView):
    def post(self, request):
        
        serializer = CommentSerializer(data=request.POST)
        
        if serializer.is_valid():
            
            comment = serializer.save(commit=False)
            comment.writer = request.user
            comment.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


### hashtag
class HashTagWrite(APIView):
    def post(self, request):
        
        serializer = HashtagSerializer(data=request.POST)
        
        if serializer.is_valid():
            
            hashtag = serializer.save(commit=False)
            hashtag.writer = request.user
            hashtag.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

