from django.db import models
from django.conf import settings
from utils import uuid_upload_to

class Disease(models.Model):
    ad_name = models.CharField(max_length=60)
    ad_category = models.CharField(max_length=60)
    ad_definition = models.TextField(blank=True)
    ad_treatment = models.TextField(blank=True)

    def __str__(self):
        return self.ad_name


class Symptom(models.Model):
    ds_id = models.CharField(max_length=60, primary_key=True, verbose_name='증상 ID')
    ds_name = models.CharField(max_length=60, verbose_name='질병명')
    ds_last = models.BooleanField(default=False)

    def __str__(self):
        return self.ds_id + ' / ' + self.ds_name


class SymptomDisease(models.Model):
    ds_id = models.ForeignKey(Symptom, on_delete=models.CASCADE, verbose_name='증상 ID')
    ad_name = models.ForeignKey(Disease, on_delete=models.CASCADE, verbose_name='질병명')


class SymptomUpload(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    ds_id = models.ForeignKey(Symptom, on_delete=False, verbose_name='증상 ID', null=True)
    ds_photo = models.ImageField(blank=True, upload_to=uuid_upload_to, verbose_name='사진')
    ds_description = models.TextField(blank=True, verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)

