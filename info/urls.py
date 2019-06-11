from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tmd', views.ThisMonthDiseaseViewSet)
router.register('atlt', views.AtTimesLikeThisViewSet)
urlpatterns = [
    path('', include(router.urls)),
]