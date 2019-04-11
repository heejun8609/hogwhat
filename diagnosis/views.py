from .serializers import SymptomModelSerializer
from utils import get_cache, make_logger
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .repository import get_first_depth, get_final_depth, get_next_depth
from .service import upload_symptom_data

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
        next_depth = get_next_depth(ds_id)    
        next_depth_serializer = SymptomModelSerializer(next_depth, many=True)
        nd_res = next_depth_serializer.data
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
        user = request.user
        ds_id = str(ds_id)
        if data.get('user_key'):
            user = data.get('user_key')

        disease_list = get_final_depth(user=user, ip=ip, ds_id=ds_id)
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
        user = request.user
        
        ds_id = str(data.get('ds_id'))

        if data.get('user_key'):
            user = data.get('user_key')

        ip = request.META['REMOTE_ADDR']

        if 'ds_photo' in request.FILES:
            photo = data.get('ds_photo')
            disease_list = get_final_depth(user=user, ip=ip, ds_id=ds_id, photo=photo)
        else:
            disease_list = get_final_depth(user=user, ip=ip, ds_id=ds_id)
        logger.debug('Final Depth Disease List : {}'.format(disease_list))
        return Response(disease_list, status=200)

    
class DiseaseSymptomDirect(APIView):

    def post(self, request):
        """
        증상에 대한 정보를 서술형으로 받는다.

        <p><b>user_key [STRING]: </b>사용자 key</p>
        <p><b>ds_desc [STRING]: </b>증상 설명</p>
        <p><b>ds_photo [MULTIPART/FORM-DATA]: </b>(선택) 업로드 사진</p>
        """
        # try:
        data = request.data
        user = request.user

        if data.get('user_key'):
            user = data.get('user_key')

        ip = request.META['REMOTE_ADDR']
        desc = data.get('ds_desc')
        
        if 'ds_photo' in request.FILES:
            photo = data.get('ds_photo')
            upload_symptom_data(user=user, ip=ip, desc=desc, photo=photo)
        else:
            upload_symptom_data(user=user, ip=ip, desc=desc)
        logger.debug('Direct Symptom Process')
        return Response(status=200)

        # except Exception as e:
        #     exception_msg = str(e.args[0])
        #     logger.exception(e)
        #     result = {"error": {"code": 500,"msg": "FAIL"},"data": {'msg': exception_msg}}
        #     return Response(result)


