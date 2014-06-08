from rest_framework import serializers
from models import ApiToken


class ApiTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiToken
