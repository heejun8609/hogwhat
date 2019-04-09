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
        <p><b> animal_cateogry [STRING]: </b>축종</p>
        <p><b> area [STRING]: </b>지역</p>
        <p><b> animal_count [STRING]: </b>사육두수</p>
        <p><b> phone_number [STRING]: </b>핸드폰 번호</p>
        """
        data = request.data

        if data.get('user_key'):
            user = data.get('user_key')
        else:
            user = request.user
        ip = request.META['REMOTE_ADDR']
        animal_cateogry = data.get('animal_category')
        area = data.get('area')
        animal_count = data.get('animal_count')
        if data.get('phone_number'):
            phone_number = str(data.get('phone_number'))
            upload_user_info(user, ip, animal_cateogry, area, animal_count, phone_number=phone_number)
        else:
            upload_user_info(user, ip, animal_cateogry, area, animal_count)
        logger.debug('User Info Upload')
        return Response(status=status.HTTP_200_OK)
# @login_required
def profile(request):
    return render(request, 'login.html')

# class KakaoLogin(SocialLoginView):
#     adapter_class = KakaoOAuth2Adapter