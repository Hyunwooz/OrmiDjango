from django.urls import path
from . import views
from blog.views import Index, List, Create

app_name = 'blog'

urlpatterns = [
    # path(패턴, 매핑) /blog/
    # path("", views.index), # FBV
    # 글 목록 조회
    path("", List.as_view(), name='list'),
    # 글 작성
    path("write/", Create.as_view(), name='write'),
    # 글 수정
    # 글 삭제
    # 코멘트 작성
    # 코멘트 삭제
]
