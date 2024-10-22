from rest_framework.schemas.coreapi import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from django.contrib.auth import get_user_model


class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        read_only_fields = ["id"]
        write_only_fields = ["password"]
        fields = (
            ["email", "first_name", "last_name"] + read_only_fields + write_only_fields
        )


class UserSinginSerializer(Serializer):
    email = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)
    first_name = serializers.CharField(max_length=255, read_only=True)
    last_name = serializers.CharField(max_length=255, read_only=True)
