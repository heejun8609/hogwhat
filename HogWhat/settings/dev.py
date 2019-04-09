from .common import *

INSTALLED_APPS += [
    'rest_framework_swagger',
    'debug_toolbar',
    # 'rest_auth',
    # 'rest_auth.registration',
    # 'allauth',
    # 'allauth.account',    
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.kakao',
]

MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE


INTERNAL_IPS = ['127.0.0.1'] # swagger 접속 ip