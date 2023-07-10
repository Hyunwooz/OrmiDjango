from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # user/register
    # 회원가입
    path("register/", views.Registration.as_view(), name='register'),
    # # 로그인
    path("login/", views.Login.as_view(), name="login"),
    # # 로그아웃
    path("logout/", views.Logout.as_view(), name='logout'),
    path("profile/write/", views.ProfileWrite.as_view(), name='pf-write'),
    path("profile/update/", views.ProfileUpdate.as_view(), name='pf-update'),
    path("profile/delete/", views.ProfileDelete.as_view(), name='pf-delete'),
]
