
import requests
from .serializers import Req_Serializers
import json
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status


def get_definition(word):
    url = "http://microservice-01:8000/get-definition"
    data = {"keyword": word}
    response = requests.post(url, data=data)
    definition = None
    if response.status_code == 200:
        definition = json.loads(response.text)['definition']

    elif response.status_code == 404 or response.status_code == 400:
        definition = "Word not found in dictionary."
    return definition, response.status_code


@api_view(['POST'])
def snippet_list(request):

    serializer = Req_Serializers(data=request.data)
    if serializer.is_valid():
        word = serializer.data['word'].strip().lower()
        definition, status_code = get_definition(word)
        if status_code == 200:
            return Response({"word":request.data['word'], "definition": definition}, status=status.HTTP_200_OK)
        else:
            return Response({"word":request.data['word'], "error": definition }, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"word": None, "error":"Invalid JSON input."}, status=status.HTTP_201_CREATED)
