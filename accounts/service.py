from utils import make_logger
from .models import User, UserInfo

logger = make_logger('USER_INFO')

def upload_user_info(user, ip, species, area, scale, **kwargs):

    user, created = User.objects.get_or_create(username=user)

    if created:
        user_info = UserInfo(user=user)
    else:
        user_info = UserInfo(user=user)

    # 유저 정보 업로드
    user_info.ip = ip
    user_info.species = species
    user_info.area = area
    user_info.scale = scale

    # 핸드폰 번호 있을 경우
    if 'phone' in kwargs:
        user_info.phone = kwargs['phone']

    user_info.save()    
    logger.debug('User Info Upload')