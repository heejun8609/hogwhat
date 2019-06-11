from rest_framework.serializers import ModelSerializer
from .models import UserInfo
# from rest_framework.authtoken.models import Token

class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('species', 'area', 'scale', 'phone')
        
# class TokenSerializer(ModelSerializer):
#     class Meta:
#         model = Token
#         fields = '__all__'
