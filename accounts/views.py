# from rest_auth.registration.views import SocialLoginView
# from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils import make_logger, get_user_token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .service import upload_user_info
from .serializers import UserInfoSerializer
from .models import UserInfo
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.conf import settings

logger = make_logger('LOGIN_VIEW')


class TokenView(APIView):
    def get(self, request, user_key):
        """
        사용자 key를 받고 토큰(key)을 반환한다.
        <p><b> user_key [STRING]: </b>사용자 key</p>
        """
        user, user_created, token = get_user_token(user_key)
        if token.get('key'):
            logger.debug('Get Token')
        return Response(token, status=200)

class UserInfoViewSet(ModelViewSet):
    """
    사용자 정보(축종, 지역, 사육두수, 핸드폰 번호)를 받는다.

    <p><b> species [STRING]: </b>축종</p>
    <p><b> area [STRING]: </b>지역</p>
    <p><b> scale [STRING]: </b>사육두수</p>
    <p><b> phone [STRING]: </b>핸드폰 번호</p>
    """
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            species = self.request.data.get('species'),
            area=self.request.data.get('area'),
            scale=self.request.data.get('scale'),
            phone=self.request.data.get('phone'),
        )
        logger.debug('User Info Upload')



# @login_required
# def profile(request):
#     return render(request, 'login.html')

# class KakaoLogin(SocialLoginView):
#     adapter_class = KakaoOAuth2Adapter