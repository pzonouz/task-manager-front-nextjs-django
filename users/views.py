from rest_framework.request import Request
from rest_framework.views import APIView, Response

from django.contrib.auth import authenticate, get_user_model

from .serializers import UserSignupSerializer, UserSinginSerializer


class signin(APIView):
    def post(self, request: Request):
        serializer = UserSinginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        if user is None:
            return Response(status=401)
        return Response(data=UserSinginSerializer(user).data, status=200)


class signup(APIView):
    def post(self, request: Request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        get_user_model().objects.create_user(**serializer.validated_data)
        return Response(status=200)
