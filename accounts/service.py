from utils import make_logger
from .models import User, UserInfo

logger = make_logger('USER_INFO')

def upload_user_info(user, ip, animal_cateogry, area, animal_count, **kwargs):

    user, created = User.objects.get_or_create(username=user)

    if created:
        user_info = UserInfo(user=user)
    else:
        user_info = UserInfo(user=user)

    # 유저 정보 업로드
    user_info.ip = ip
    user_info.animal_cateogry = animal_cateogry
    user_info.area = area
    user_info.animal_count = animal_count

    # 핸드폰 번호 있을 경우
    if 'phone_number' in kwargs:
        user_info.phone_number = kwargs['phone_number']

    user_info.save()    
    logger.debug('User Info Upload')