from django.urls import path
# from . import views
from blog.views import Index, List, Write, Update, Delete, DetailView,CommentWrite,CommentDelete,HashTagWrite,HashTagDelete

app_name = 'blog'

urlpatterns = [
    # path(패턴, 매핑) /blog/
    # path("", views.index), # FBV
    # 글 목록 조회
    path("", List.as_view(), name='list'), # /blog/
    # 글 상세 조회
    # path("detail/<int:pk>/", Detail.as_view(), name='detail'),
    path("detail/<int:pk>/", DetailView.as_view(), name='detail'),
    # 글 작성
    path("write/", Write.as_view(), name='write'), # /blog/write/
    # 글 수정
    path("detail/<int:pk>/edit", Update.as_view(), name='edit'),
    # 글 삭제
    path("detail/<int:pk>/delete", Delete.as_view(), name='delete'),
    # 코멘트 작성
    path("detail/<int:pk>/comment/write", CommentWrite.as_view(), name='cm-write'),
    # 코멘트 삭제
    path("detail/comment/<int:pk>/delete", CommentDelete.as_view(), name='cm-delete'),
    # 태그 작성
    path("detail/<int:pk>/hashtag/write", HashTagWrite.as_view(), name='tag-write'),
    # 태그 삭제
    path("detail/hashtag/<int:pk>/delete", HashTagDelete.as_view(), name='tag-delete'),
]
