from rest_framework.serializers import ModelSerializer
from .models import *

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields=['name','bio']


class AdvocateSerializers(ModelSerializer):
    company=CompanySerializer()
    class Meta:
        model = Advocate
        fields = ['username', 'bio','company']


