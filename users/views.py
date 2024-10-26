from uuid import uuid4

from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView, Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate, get_user_model

from .serializers import SocialSerializer, UserSignupSerializer, UserSinginSerializer


class Signin(APIView):
    def post(self, request: Request):
        serializer = UserSinginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            return Response(
                {
                    "access": str(access),
                    "refresh": str(refresh),
                    "email": UserSinginSerializer(user).data.get("email", ""),
                    "image": UserSinginSerializer(user).data.get("image", ""),
                    "first_name": UserSinginSerializer(user).data.get("first_name", ""),
                    "last_name": UserSinginSerializer(user).data.get("last_name", ""),
                },
                status=200,
            )
        return Response(status=400)


class Signup(APIView):
    def post(self, request: Request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        get_user_model().objects.create_user(**serializer.validated_data)
        return Response(status=200)


class Social(APIView):
    def post(self, request: Request):
        existing_user = (
            get_user_model().objects.filter(email=request.data["email"]).first()
        )
        if existing_user is None:
            request.data["social"] = True
            serializer = SocialSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data["password"] = uuid4().hex
            user = get_user_model().objects.create_user(**serializer.validated_data)
            user.save()
            return Response(status=200)
        existing_user.social = True
        existing_user.first_name = request.data["first_name"]
        existing_user.last_name = request.data["last_name"]
        existing_user.save()
        return Response(status=200)


class GetUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        print(request.user)
        return Response(200)
