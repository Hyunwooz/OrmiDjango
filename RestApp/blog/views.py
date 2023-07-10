from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment, HashTag
from .forms import PostForm
from .serializers import PostSerializer, CommentSerializer, HashtagSerializer


### post
class Index(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialized_posts = PostSerializer(posts, many=True) # 직렬화
        return Response(serialized_posts.data)


class Write(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.POST)
        if serializer.is_valid():
            post = serializer.save(writer=request.user)
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Update(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Delete(APIView):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response({'message': 'Post deleted'}, status=status.HTTP_200_OK)
### Comment
class CommentWrite(APIView):
    def post(self, request, pk):
        serializer = CommentSerializer(data=request.POST)
        
        if serializer.is_valid():
            
            comment = serializer.save(writer=request.user)
            comment.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


### hashtag
class HashTagWrite(APIView):
    def post(self, request, pk):
        
        serializer = HashtagSerializer(data=request.POST)
        
        if serializer.is_valid():
            
            hashtag = serializer.save(writer=request.user)
            hashtag.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDelete(APIView):
    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

class HashTagDelete(APIView):
    def post(self, request, pk):
        hashtag = HashTag.objects.get(pk=pk)
        hashtag.delete()
        serializer = HashtagSerializer(hashtag)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)