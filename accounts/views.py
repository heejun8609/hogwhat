# from rest_auth.registration.views import SocialLoginView
# from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils import make_logger
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .service import upload_user_info

logger = make_logger('LOGIN_VIEW')

class UserInfoView(APIView):
    def post(self, request):
        """
        사용자 정보를 받는다.

        <p><b> user_key [STRING]: </b>사용자 key</p>
        <p><b> species [STRING]: </b>축종</p>
        <p><b> area [STRING]: </b>지역</p>
        <p><b> scale [STRING]: </b>사육두수</p>
        <p><b> phone [STRING]: </b>핸드폰 번호</p>
        """
        data = request.data

        if data.get('user_key'):
            user = data.get('user_key')
        else:
            user = request.user
        ip = request.META['REMOTE_ADDR']
        species = data.get('species')
        area = data.get('area')
        scale = data.get('scale')
        if data.get('phone'):
            phone = str(data.get('phone'))
            upload_user_info(user, ip, species, area, scale, phone=phone)
        else:
            upload_user_info(user, ip, species, area, scale)
        logger.debug('User Info Upload')
        return Response(status=200)

        
# @login_required
def profile(request):
    return render(request, 'login.html')

# class KakaoLogin(SocialLoginView):
#     adapter_class = KakaoOAuth2Adapter