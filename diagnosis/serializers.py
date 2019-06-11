from rest_framework.serializers import ModelSerializer
from .models import Disease, Symptom, SymptomDisease, SymptomUpload, SymptomPhoto, SymptomDescription

class DiseaseModelSerializer(ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'

class SymptomModelSerializer(ModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'

class SymptomDiseaseModelSerializer(ModelSerializer):
    class Meta:
        model = SymptomDisease
        fields = '__all__'

class SymptomUploadModelSerializer(ModelSerializer):
    class Meta:
        model = SymptomUpload
        fields = ('ds_id',)

class SymptomPhotoModelSerializer(ModelSerializer):
    class Meta:
        model = SymptomPhoto
        fields = ('ds_photo',)

class SymptomDescriptionModelSerializer(ModelSerializer):
    class Meta:
        model = SymptomDescription
        fields = ('ds_description',)