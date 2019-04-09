from django.urls import path, include
from . import views

urlpatterns = [
    path('tmd/', views.ThisMonthDiseaseInfo.as_view()),
    path('atlt/', views.AtTimesLikeThisInfo.as_view()),
]