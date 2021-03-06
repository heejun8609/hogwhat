from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as AuthUserManager
from django.conf import settings


class UserManager(AuthUserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        # extra_fields.setdefault('sex', 'm')
        return super().create_superuser(username, email, password, **extra_fields)

class User(AbstractUser):
    # sex = models.CharField(max_length=1, choices=(('f', 'female'), ('m', 'male')), verbose_name='성별')
    pass


class UserInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    species = models.CharField(max_length=60, verbose_name='축종')
    area = models.CharField(max_length=60, verbose_name='지역')
    scale = models.CharField(max_length=60, verbose_name='사육두수')
    phone = models.CharField(max_length=60, verbose_name='휴대전화번호', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# class TagRelation(models.Model):
    # tags = models.CharField(max_length=100, blank=True)
    # tag_set = models.ManyToManyField('Tag', blank=True)


# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     def __str__(self):
#         return self.name

