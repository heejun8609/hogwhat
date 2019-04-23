from .serializers import SymptomUploadModelSerializer, SymptomDiseaseModelSerializer, DiseaseModelSerializer, SymptomPhotoModelSerializer, SymptomDescriptionModelSerializer
from utils import make_logger
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .repositories import get_first_depth, get_final_depth, get_next_depth
from .models import SymptomUpload, SymptomDisease, Disease, Symptom, SymptomPhoto, SymptomDescription
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from accounts.models import User
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

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
        disease_list = get_final_depth(ds_id=ds_id)
        logger.debug('Final Depth Disease List : {}'.format(disease_list))
        return Response(disease_list, status=200)

class DirectDescription(APIView):
    def post(self, request):
        """
        직접 문의하기 텍스트를 가져온다.

        <p><b>su_id [STRING/INT]: </b>직접 문의하기 작성 텍스트 id</p>
        """

        data = request.data
        su_id = data.get('su_id')
        symptom_description = SymptomDescription.objects.get(su_id=su_id)
        sdm_srializer = SymptomDescriptionModelSerializer(symptom_description)
        logger.debug('Direct Description : {}'.format(sdm_srializer.data))
        return Response(sdm_srializer.data, status=200)

class DiseaseSymptomViewSet(ModelViewSet):
    """
    사용자가 등록한 증상 데이터를 업로드한다.

    <p><b>ds_id [STRING/INT]: </b>선택 증상 id</p>
    <p><b>ds_desc [STRING]: </b>(선택) 증상 설명</p>
    <p><b>ds_photo [MULTIPART/FORM-DATA]: </b>(선택) 업로드 사진</p>
    """
    queryset = SymptomUpload.objects.all()
    serializer_class = SymptomUploadModelSerializer
    authentication_classes = [TokenAuthentication]
    http_method_names = ['post']
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = JSONWebTokenAuthentication().authenticate(self.request)
        ip = self.request.META['REMOTE_ADDR']
        ds_id = Symptom.objects.get(ds_id=self.request.data.get('ds_id'))
        self.perform_create(serializer.save(user=user, ip=ip, ds_id=ds_id))
        headers = self.get_success_headers(serializer.data)
        logger.debug('Single Process Upload')


        su_obj = self.get_queryset().filter(user=user, ip=ip,ds_id=ds_id).last() 

        if request.data.get('ds_photo'):
            spm_serializer = SymptomPhotoModelSerializer(data=request.data)
            ds_photo = request.data.get('ds_photo')
            if spm_serializer.is_valid():
                spm_serializer.save(
                    su_id=su_obj,
                    ds_photo=ds_photo,
                )
                logger.debug('Photo Upload')

        if request.data.get('ds_desc'):
            ds_desc = request.data.get('ds_desc')
            sdm_serializer = SymptomDescriptionModelSerializer(data=request.data)
            if sdm_serializer.is_valid():
                sdm_serializer.save(
                    su_id=su_obj,
                    ds_description=ds_desc,
                )
                logger.debug('Description Upload')

        return Response(su_obj.id, status=status.HTTP_201_CREATED, headers=headers)