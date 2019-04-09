from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .repository import DiseaseInfoRepo
import logging 
from utils import get_cache, make_logger

logger = make_logger('INFO_VIEW')

class ThisMonthDiseaseInfo(APIView):

    def get(self, request):
        """
        '이 달의 질병'을 조회한다.
        """
        di_repo = get_cache('dir_cache', DiseaseInfoRepo())
        # try:
        tmd_serializer = di_repo.get_this_month_disease()
        return Response(tmd_serializer.data, status=status.HTTP_200_OK)

        # except Exception as e:
        #     exception_msg = str(e.args[0])
        #     logger.exception(e)
        #     result = {"error": {"code": 500,"msg": "FAIL"},"data": {'msg': exception_msg}}
        #     return Response(result)


class AtTimesLikeThisInfo(APIView):

    def get(self, request):
        """
        '이럴땐 이렇게'를 조회한다.
        """
        di_repo = get_cache('dir_cache', DiseaseInfoRepo())

        # try:
        atlt_serializer = di_repo.get_at_times_like_this()
        return Response(atlt_serializer.data, status=status.HTTP_200_OK)

        # except Exception as e:
        #     exception_msg = str(e.args[0])
        #     logger.exception(e)
        #     result = {"error": {"code": 500,"msg": "FAIL"},"data": {'msg': exception_msg}}
        #     return Response(result)