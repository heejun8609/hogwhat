
from .models import Disease, Symptom, SymptomDisease, SymptomUpload
from .serializers import DiseaseModelSerializer, SymptomModelSerializer
from django.db.models import Q
from django.shortcuts import get_object_or_404
from utils import get_cache
import logging
from os.path import basename
from diagnosis.service import upload_symptom_data
from accounts.models import User

def get_first_depth():
    symptom_queryset = get_cache('symptom_cache', Symptom.objects.all())
    first_depth = symptom_queryset.filter(ds_id__regex="^[1-9]{1}$")
    first_depth_serializer = SymptomModelSerializer(first_depth, many=True)
    return first_depth_serializer


def get_next_depth(ds_id):
    symptom_queryset = get_cache('symptom_cache', Symptom.objects.all())
    ds_id_length = len(ds_id) + 1
    filter_Q = Q(ds_id__startswith=ds_id) & Q(ds_id__regex="^[1-9]{%s}$" % (ds_id_length))
    next_depth = symptom_queryset.filter(filter_Q)
    next_depth_serializer = SymptomModelSerializer(next_depth, many=True)
    next_depth_serializer = next_depth_serializer.data
    return next_depth_serializer
    

def get_final_depth(ip, ds_id, **kwargs):
    symptom_disease_queryset = get_cache('symptom_disease_cache', SymptomDisease.objects.all())
    disease_list = []
    final_depth =symptom_disease_queryset.filter(ds_id=ds_id)
    username = kwargs['user_name']
    user = User.objects.filter(username=username)
    # 질병 정보 가져오기
    for q in final_depth:
        disease_queryset = get_object_or_404(Disease, id=q.ad_name_id)
        final_depth_serializer = DiseaseModelSerializer(disease_queryset)
        disease_list.append(final_depth_serializer.data)
    
    if 'photo' in kwargs:
        upload_symptom_data(username=username, ip=ip, photo=kwargs['photo'])
    else:
        upload_symptom_data(username=username, ip=ip)

    return disease_list