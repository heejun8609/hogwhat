from .serializers import SymptomUploadModelSerializer, SymptomDiseaseModelSerializer, DiseaseModelSerializer
from utils import get_cache, make_logger
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .repositories import get_first_depth, get_final_depth, get_next_depth
from .models import SymptomUpload, SymptomDisease, Disease, Symptom
from .service import upload_symptom_data
from rest_framework.decorators import list_route, detail_route, action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from accounts.models import User

logger = make_logger('DIAGNOSIS_VIEW')


class DiseaseSymptom(APIView):
    
    def get(self, request):
        """
        First Depth 증상 리스트를 보여준다.

        <p><b>ds_id [STRING/INT]: </b>선택 증상 id</p>
        """
        first_depth_serializer = get_first_depth()
        fd_res = first_depth_serializer.data
        logger.debug('First Depth Symptom List : {}'.format(fd_res))
        return Response(fd_res, status=200)


    def post(self, request):
        """
        Next Depth 증상 리스트를 보여준다.
        특정 'ds_id'의 ds_last'가 True일 경우, 그 'ds_id'가 Final Depth이다.

        <p><b>ds_id [STRING/INT]: </b>선택 증상 id</p>
        """
        data = request.data
        ds_id = str(data.get('ds_id'))
        nd_res = get_next_depth(ds_id)    
        logger.debug('Next Depth Symtom List : {}'.format(nd_res))
        return Response(nd_res, status=200)

      
class DiseaseTreatment(APIView):
    def get(self, request, ds_id):
        """
        최종 증상을 선택하면 질병/치료 정보를 가져온다.

        <p><b>ds_id [STRING/INT]: </b>선택 증상 id</p>
        """
        ip = request.META['REMOTE_ADDR']
        data = request.data
        ds_id = str(ds_id)
        disease_list = get_final_depth(ip=ip, ds_id=ds_id)
        logger.debug('Final Depth Disease List : {}'.format(disease_list))
        return Response(disease_list, status=200)


class DiseaseTreatmentUpload(APIView):
    def post(self, request):
        """
        최종 증상을 선택하면 질병/치료 정보를 가져오고, 사용자가 등록한 데이터를 업로드한다.

        <p><b>user_key [STRING]: </b>사용자 key</p>
        <p><b>ds_id [STRING/INT]: </b>선택 증상 id</p>
        <p><b>ds_photo [MULTIPART/FORM-DATA]: </b>(선택) 업로드 사진</p>
        """
        data = request.data
        if data.get('user_key'):
            user_name = data.get('user_key')
        else:
            user_name = 'aidkr'
        ds_id = str(data.get('ds_id'))
        ip = request.META['REMOTE_ADDR']
        disease_list = get_final_depth(ds_id)
        if 'ds_photo' in request.FILES:
            photo = data.get('ds_photo')
            upload_symptom_data(username=user_name, ip=ip, ds_id=ds_id, photo=photo)
            
        else:
            upload_symptom_data(username=user_name, ip=ip, ds_id=ds_id)
        logger.debug('Final Depth Disease List : {}'.format(disease_list))
        return Response(disease_list, status=200)


class DiseaseSymptomViewSet(ModelViewSet):
    """
    사용자가 등록한 증상 데이터를 업로드한다.

    <p><b>ds_id [STRING/INT]: </b>선택 증상 id</p>
    <p><b>ds_desc [STRING]: </b>증상 설명</p>
    <p><b>ds_photo [MULTIPART/FORM-DATA]: </b>(선택) 업로드 사진</p>
    """
    queryset = SymptomUpload.objects.all()
    serializer_class = SymptomUploadModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            ip=self.request.META['REMOTE_ADDR'],
            ds_id=Symptom.objects.get(ds_id=self.request.data.get('ds_id')),
            ds_description=self.request.data.get('ds_desc'),
            ds_photo=self.request.data.get('ds_photo'),
        )
        logger.debug('Direct Symptom Process')

