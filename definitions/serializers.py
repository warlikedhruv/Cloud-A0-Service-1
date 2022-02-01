from rest_framework import serializers


class Req_Serializers(serializers.Serializer):
    word = serializers.CharField(max_length=1000)