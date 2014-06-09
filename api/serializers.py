from rest_framework import serializers
from models import ApiToken, APIKeyInfo


class ApiTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiToken

class APIKeyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKeyInfo
