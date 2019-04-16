from utils import get_anonymous_permission, get_cache, make_logger
from django.core.files import File
from .models import Symptom, SymptomUpload
from accounts.models import User

logger = make_logger('UPLOAD')

def upload_symptom_data(username, ip, ds_id, **kwargs):
    symptom_queryset = get_cache('symptom_cache', Symptom.objects.all())
    symptom_ds_id = symptom_queryset.get(ds_id=ds_id)

    # 익명 유저일 경우 모델에 대한 권한 추가
    user, created = User.objects.get_or_create(username=username)
    symptom_upload = SymptomUpload(user=user)
    symptom_upload.ip = ip
    symptom_upload.ds_id = symptom_ds_id

    # 업로드 이미지 있을 경우
    if 'photo' in kwargs:
        photo = kwargs['photo']
        symptom_upload.ds_photo.save(str(photo), photo, save=True)
        logger.debug('Symptom Process Image Upload')
    
    # 업로드 증상 상세 설명 있을 경우
    if 'desc' in kwargs:
        symptom_upload.ds_description = kwargs['desc']
    
    symptom_upload.save()    
    logger.debug('Disease Symptom Process Upload')