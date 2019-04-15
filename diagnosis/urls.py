from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('direct', views.DiseaseSymptomViewSet)
# router.register('treatment', views.DiseaseTreatmentViewSet)

urlpatterns = [
    path('', views.DiseaseSymptom.as_view()),
    path('', include(router.urls)),
    path('treatment/<ds_id>/', views.DiseaseTreatment.as_view()),
    path('treatment/', views.DiseaseTreatmentUpload.as_view()),
]

# urlpatterns = [
#     path('', views.DiseaseSymptom.as_view()),
#     path('direct/', views.DiseaseSymptomDirect.as_view()),
#     path('treatment/', views.DiseaseTreatmentUpload.as_view()),
#     path('treatment/<ds_id>/', views.DiseaseTreatment.as_view()),
# ]