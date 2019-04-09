from django.urls import path
import django.contrib.auth.views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('user-info/', views.UserInfoView.as_view()),
    # path('rest-auth/kakao/', views.KakaoLogin.as_view(), name='k_login'),
]