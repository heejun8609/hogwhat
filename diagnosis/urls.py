from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('direct', views.DiseaseSymptomViewSet)

urlpatterns = [
    path('', views.DiseaseSymptom.as_view()),
    path('', include(router.urls)),
    path('treatment/<ds_id>/', views.DiseaseTreatment.as_view()),
    path('treatment/', views.DiseaseTreatmentUpload.as_view()),
]