# from rest_auth.registration.views import SocialLoginView
# from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils import make_logger, get_jwt_token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserInfoSerializer
from .models import UserInfo, User
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

logger = make_logger('LOGIN_VIEW')


class UserInfoViewSet(ModelViewSet):
    """
    [POST] 사용자 정보(축종, 지역, 사육두수, 핸드폰 번호)를 등록한다.

    <p><b> species [STRING]: </b>축종</p>
    <p><b> area [STRING]: </b>지역</p>
    <p><b> scale [STRING]: </b>사육두수</p>
    <p><b> phone [STRING]: </b>핸드폰 번호</p>
    """
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    authentication_classes = [TokenAuthentication]
    http_method_names = ['post']

    def perform_create(self, serializer):
        (user, token) = JSONWebTokenAuthentication().authenticate(self.request)
        serializer.save(
            user=user,
            species = self.request.data.get('species'),
            area=self.request.data.get('area'),
            scale=self.request.data.get('scale'),
            phone=self.request.data.get('phone'),
        )
        logger.debug('User Info Upload')


class UserInfoCheckView(APIView):
    def get(self, request, device_id):
        """
        사용자 Device Id를 받고 사용자 정보 등록 여부 확인하여 True, False로 Response를 보낸다.
        <p><b> device_id [STRING]: </b>사용자 device_id</p>
        """
        try:
            user = get_object_or_404(User, username=device_id)
            is_userinfo = bool(user.userinfo_set.all())
            return Response(is_userinfo, status=200)
        except ObjectDoesNotExist as e:
            msg = "Token을 먼저 받으세요"
            logger.debug(msg)
            return Response({'result': 'fail', 'msg': msg}, status=status.HTTP_404_NOT_FOUND)

class JWTView(APIView):
    def get (self, request, device_id):
        """
        사용자 Device Id 받고 토큰(key)을 반환한다.
        <p><b> device_id [STRING]: </b>사용자 device_id</p>
        """
        token = get_jwt_token(device_id)
        logger.debug('Get Token')
        return Response(token, status=200)
        

# class TokenView(APIView):
#     def get(self, request, device_id):
#         """
#         사용자 Device Id 받고 토큰(key)을 반환한다.
#         <p><b> device_id [STRING]: </b>사용자 device_id</p>
#         """
#         User
#         user, user_created, token = get_user_token(device_id)
#         if token.get('key'):
#             logger.debug('Get Token')
#         return Response(token, status=200)


# @login_required
# def profile(request):
#     return render(request, 'login.html')

# class KakaoLogin(SocialLoginView):
#     adapter_class = KakaoOAuth2Adapter