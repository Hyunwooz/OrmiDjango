from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Index Page GET')
#     # 나머지 요청
#     # 에러, 예외처리
#     return HttpResponse('No')


class Index(View):
    def get(self, request):
        # return HttpResponse('Index Page Get')
        
        # 데이터베이스에 접근해서 값을 가져와야 합니다.
        # 게시판에 글들을 보여줘야하기 때문에 데이터베이스에서 "값 조회"
        post_objs = Post.objects.all()
        # context = 데이터베이스에서 가져온 값
        context = {
            "posts": post_objs
        }
        return render(request, 'blog/board.html', context)


# write
# post - form
# 글 작성 화면
# def write(request):
#     if request.method == "POST":
#         # form 확인
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             return redirect('blog:list')
        
#     form = PostForm()
#     return render(request, 'blog/write.html', {'form': form})


# Django 자체의 클래스 뷰 기능도 강력, 편리
# django.views.generic -> ListView
class List(ListView):
    model = Post
    context_object_name = 'post_list'


class Create(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:list')