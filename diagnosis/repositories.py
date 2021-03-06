
from .models import Disease, Symptom, SymptomDisease
from .serializers import DiseaseModelSerializer, SymptomModelSerializer
from django.db.models import Q
from django.shortcuts import get_object_or_404
import logging
from os.path import basename
from accounts.models import User
import functools

@functools.lru_cache()
def get_first_depth():
    symptom_queryset =  Symptom.objects.all()
    first_depth = symptom_queryset.filter(ds_id__regex="^[1-9]{1}$")
    first_depth_serializer = SymptomModelSerializer(first_depth, many=True)
    return first_depth_serializer

@functools.lru_cache()
def get_next_depth(ds_id):
    symptom_queryset = Symptom.objects.all()
    ds_id_length = len(ds_id) + 1
    filter_Q = Q(ds_id__startswith=ds_id) & Q(ds_id__regex="^[1-9]{%s}$" % (ds_id_length))
    next_depth = symptom_queryset.filter(filter_Q)
    next_depth_serializer = SymptomModelSerializer(next_depth, many=True)
    next_depth_serializer = next_depth_serializer.data
    return next_depth_serializer
    
@functools.lru_cache()
def get_final_depth(ds_id):
    symptom_disease_queryset = SymptomDisease.objects.all()
    disease_list = []
    final_depth =symptom_disease_queryset.filter(ds_id=ds_id)
    
    # 질병 정보 가져오기
    for q in final_depth:
        disease_queryset = get_object_or_404(Disease, id=q.ad_name_id)
        final_depth_serializer = DiseaseModelSerializer(disease_queryset)
        disease_list.append(final_depth_serializer.data)
    return disease_list