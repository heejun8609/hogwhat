from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
# from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

schema_view = get_swagger_view(title='동물 질병/증상 API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/', schema_view),
    path('accounts/', include('accounts.urls')),
    path('symptom/', include('diagnosis.urls')),
    path('info/', include('info.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework ')),
    # path('api-token-auth/', obtain_auth_token),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('api-jwt-auth/', obtain_jwt_token),
    # path('api-jwt-auth/refresh', refresh_jwt_token),
    # path('api-jwt-auth/verify', verify_jwt_token),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
