from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse

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
# model, template_name, context_object_name,
# paginate_by, form_class, form_valid(), get_queryset()
# django.views.generic -> ListView


class List(ListView):
    model = Post # 모델
    template_name = 'blog/post_list.html' # 템플릿
    context_object_name = 'posts' # 변수 값의 이름


class Write(CreateView):
    model = Post # 모델
    form_class = PostForm # 폼
    success_url = reverse_lazy('blog:list') # 성공시 보내줄 url


class Detail(DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class Update(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']
    # success_url = reverse_lazy('blog:list')
    
    # initial 기능 사용 -> form에 값을 미리 넣어주기 위해서
    def get_initial(self):
        initial = super().get_initial() # UpdateView.get_initial()
        post = self.get_object() # pk 기반으로 객체를 가져옴
        initial['title'] = post.title
        initial['content'] = post.content
        return initial

    def get_success_url(self):
        post = self.get_object() # pk 기반으로 현재 객체 가져오기
        return reverse('blog:detail', kwargs={'pk':post.pk})


class Edit(UpdateView):
    model = Post
    template_name = 'blog/post_edit2.html'
    context_object_name = 'post'
    form_class = PostForm # 폼
    
    def get_success_url(self):
        post = self.get_object() # pk 기반으로 현재 객체 가져오기
        return reverse('blog:detail', kwargs={'pk':post.pk})