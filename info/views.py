from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import detail_route
from .serializers import ThisMonthDiseaseModelSerializer, AtTimesLikeThisModelSerializer
from .models import ThisMonthDisease, AtTimesLikeThis
from utils import make_logger


logger = make_logger('INFO_VIEW')

class ThisMonthDiseaseViewSet(ReadOnlyModelViewSet):
    """
    '이 달의 질병'을 조회한다.
    """
    queryset = ThisMonthDisease.objects.all()
    serializer_class = ThisMonthDiseaseModelSerializer
    http_method_names = ['get']

    def get_queryset(self):
        qs = super().get_queryset().filter(pk=1)
        return qs

    @detail_route()
    def tmd(self, request):
        qs = self.queryset.filter(pk=1)
        serializer = self.get_serializer(qs, many=True)
        logger.debuger("TMD : ", serializer.data)
        return Response(serializer.data, status=200)
        

class AtTimesLikeThisViewSet(ReadOnlyModelViewSet):
    """
    '이럴땐 이렇게'를 조회한다.
    """
    queryset = AtTimesLikeThis.objects.all()
    serializer_class = AtTimesLikeThisModelSerializer
    http_method_names = ['get']

    def get_queryset(self):
        qs = super().get_queryset().filter(pk=1)
        return qs

    @detail_route()
    def atlt(self, request):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        logger.debuger("ATLT : ", serializer.data)
        return Response(serializer.data, status=200)
