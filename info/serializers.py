from rest_framework.serializers import ModelSerializer
from .models import ThisMonthDisease, AtTimesLikeThis

class ThisMonthDiseaseModelSerializer(ModelSerializer):
    class Meta:
        model = ThisMonthDisease
        fields = '__all__'


class AtTimesLikeThisModelSerializer(ModelSerializer):
    class Meta:
        model = AtTimesLikeThis
        fields = '__all__'