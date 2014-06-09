from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import ApiToken, APIKeyInfo
from serializers import ApiTokenSerializer, APIKeyInfoSerializer
from eveapi import EveAPI
import logging


log = logging.getLogger(__name__)

@api_view(['GET'])
def api_token_list(request, user_id):
    """
    List all API tokens for a user
    :param request:
    :param user_id:
    :return:
    """
    if request.method == 'GET':
        api_tokens = ApiToken.objects.get(user_id=user_id)
        serializer = ApiTokenSerializer(api_tokens)
        return Response(serializer.data)

@api_view(['GET'])
def api_key_info_list(request):
    api_key_info = APIKeyInfo.objects.all()
    serializer = APIKeyInfoSerializer(api_key_info, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_key_info_retrieve(request, api_token_id):
    try:
        api_key_info = APIKeyInfo.objects.get(apiToken_id=api_token_id)
    except APIKeyInfo.DoesNotExist:
        log.info('API key information not found in database, fetching from API')
        api_token = ApiToken.objects.get(id=api_token_id)
        eveapi = EveAPI(api_token.keyId, api_token.verificationCode)
        key_info = eveapi.account.apiKeyInfo()


    serializer = APIKeyInfoSerializer(api_key_info)
    return Response(serializer.data)