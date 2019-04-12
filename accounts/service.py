from utils import make_logger, get_user_token
from .models import User, UserInfo

logger = make_logger('USER_INFO')

def upload_user_info(user_name, ip, species, area, scale, **kwargs):
    user, user_created, token = get_user_token(user_name)

    if token.get('key'):
        logger.debug('Get Token')

    if user_created:
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

    # 유저 토큰 생성 또는 불러오기

    return token