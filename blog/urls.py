from django.urls import path
# from . import views
from blog.views import Index, List, Write, Detail

app_name = 'blog'

urlpatterns = [
    # path(패턴, 매핑) /blog/
    # path("", views.index), # FBV
    # 글 목록 조회
    path("", List.as_view(), name='list'), # /blog/
    # 글 상세 조회
    path("detail/<int:pk>/", Detail.as_view(), name='detail'),
    # 글 작성
    path("write/", Write.as_view(), name='write'), # /blog/write/
    # 글 수정
    # 글 삭제
    # 코멘트 작성
    # 코멘트 삭제
]
