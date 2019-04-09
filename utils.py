import uuid
import os
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from accounts.models import User
import logging
from django.conf import settings


def get_anonymous_permission(user, model, perm):
    content_type = ContentType.objects.get_for_model(model)
    model_name = model.__name__.lower()
    codename = '_'.join([perm, model_name])
    perm = Permission.objects.get(content_type=content_type, codename=codename)
    user.user_permissions.add(perm)
    return user


def get_cache(name, data):
    cache_data = cache.get(name)
    if cache_data is None:
        cache.set(name, data)
        return data
    return cache_data


def make_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s[%(levelname)s] - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    if os.path.exists(settings.LOGS_DIR) is False:
        os.mkdir(settings.LOGS_DIR)

    file_handler = logging.FileHandler(os.path.join(settings.LOGS_DIR, 'api-server.log'))
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger


def uuid_upload_to(instance, filename):
    ym_path = timezone.now().strftime('%Y/%m')
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return '/'.join([ym_path, uuid_name + extension])