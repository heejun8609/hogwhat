from .common import *

WSGI_APPLICATION = 'HogWhat.wsgi_dev.application'

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


INTERNAL_IPS = ['192.168.1.134', '192.168.1.131'] # swagger 접속 ip