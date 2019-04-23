from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('treatment', views.DiseaseSymptomViewSet)
router.register('direct', views.DiseaseSymptomDirectViewSet)

urlpatterns = [
    path('treatment/<ds_id>/', views.DiseaseTreatment.as_view()),
    path('get-direct/', views.DirectDescription.as_view()),
    path('', views.DiseaseSymptom.as_view()),
    path('', include(router.urls)),    
]