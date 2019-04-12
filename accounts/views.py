# from rest_auth.registration.views import SocialLoginView
# from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils import make_logger, get_user_token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .service import upload_user_info

from django.conf import settings

logger = make_logger('LOGIN_VIEW')

class UserView(APIView):
    def post(self, request):
        """
        사용자 정보(사용자 key, 축종, 지역, 사육두수, 핸드폰 번호)를 받고, 토큰(key)을 반환한다.

        <p><b> user_key [STRING]: </b>사용자 key</p>
        <p><b> species [STRING]: </b>축종</p>
        <p><b> area [STRING]: </b>지역</p>
        <p><b> scale [STRING]: </b>사육두수</p>
        <p><b> phone [STRING]: </b>핸드폰 번호</p>
        """
        data = request.data
        user_name = data.get('user_key')    
        ip = request.META['REMOTE_ADDR']
        species = data.get('species')
        area = data.get('area')
        scale = data.get('scale')
        if data.get('phone'):
            phone = str(data.get('phone'))
            token = upload_user_info(user_name, ip, species, area, scale, phone=phone)
        else:
            token = upload_user_info(user_name, ip, species, area, scale)
        logger.debug('User Info Upload')
        return Response(token, status=200)                 

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


# @login_required
# def profile(request):
#     return render(request, 'login.html')

# class KakaoLogin(SocialLoginView):
#     adapter_class = KakaoOAuth2Adapter