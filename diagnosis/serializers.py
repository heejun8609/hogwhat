from rest_framework.serializers import ModelSerializer
from .models import Disease, Symptom, SymptomDisease

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