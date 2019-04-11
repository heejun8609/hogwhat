from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.DiseaseSymptom.as_view()),
    path('direct/', views.DiseaseSymptomDirect.as_view()),
    path('treatment/', views.DiseaseTreatmentUpload.as_view()),
    path('treatment/<ds_id>/', views.DiseaseTreatment.as_view()),
    # path('new/', views.post_new, name='post_new')
]