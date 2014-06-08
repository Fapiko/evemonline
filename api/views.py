from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import ApiToken
from serializers import ApiTokenSerializer


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
