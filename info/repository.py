from .models import ThisMonthDisease, AtTimesLikeThis
from .serializers import ThisMonthDiseaseModelSerializer, AtTimesLikeThisModelSerializer
from django.db.models import Max
import logging
import random
from utils import get_cache

logger = logging.getLogger(__name__)


class DiseaseInfoRepo:

    def get_this_month_disease(self):
        tmd_all = ThisMonthDisease.objects.all()
        tmd_queryset = get_cache('tmd_cache', tmd_all)
        max_id = tmd_queryset.aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            tmd = tmd_queryset.filter(pk=pk).first()
            
            if tmd:
                logger.debug('This Month Disease Query : {}'.format(tmd))
                tmd_serializer = ThisMonthDiseaseModelSerializer(tmd)
                return tmd_serializer


    def get_at_times_like_this(self):
        atlt_all = AtTimesLikeThis.objects.all()
        atlt_queryset = get_cache('atlt_cache', atlt_all)
        max_id = atlt_queryset.aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            atlt = atlt_queryset.filter(pk=pk).first()
            if atlt:
                logger.debug('At Times Like This Query : {}'.format(atlt))
                atlt_serializer = AtTimesLikeThisModelSerializer(atlt)
                return atlt_serializer