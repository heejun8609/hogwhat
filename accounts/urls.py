from django.urls import path, include
import django.contrib.auth.views as auth_views
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user-info', views.UserInfoViewSet)


urlpatterns = [
    path('user-info/<device_id>/', views.UserInfoCheckView.as_view()),
    path('token/<device_id>/', views.TokenView.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path(r'', include(router.urls)),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('profile/', views.profile, name='profile'),
    # path('rest-auth/kakao/', views.KakaoLogin.as_view(), name='k_login'),
]