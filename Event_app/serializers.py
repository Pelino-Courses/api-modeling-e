from rest_framework.serializers import ModelSerializer
from . models import speaker_management

class speaker_managementSerializer(ModelSerializer):
    class Meta:
        model =  speaker_management
        fields = '__all__'
    