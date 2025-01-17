from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from api.authentication import TokenAuthentication
from .serializers import UserSerializer


### function based views
@api_view(["POST"])
def login(request):
    username = request.data["username"]
    password = request.data["password"]

    user = get_object_or_404(User, username=username)
    print(user)

    if not user.check_password(password):
        return Response({"error": "Invalid Password"}, status=HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response(
        {"token": token.key, "user": serializer.data},
        status=HTTP_200_OK,
    )


@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    serializer.save()

    username = serializer.data["username"]
    password = serializer.data["password"]

    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()

    token = Token.objects.create(user=user)

    return Response(
        {"token": token.key, "user": serializer.data},
        status=HTTP_201_CREATED,
    )


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UserSerializer(instance=request.user)
    return Response(serializer.data, status=HTTP_200_OK)


### class-based views
class LoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = get_object_or_404(User, username=username)
        print(user)

        if not user.check_password(password):
            return Response({"error": "Invalid Password"}, status=HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)

        return Response(
            {"token": token.key, "user": serializer.data},
            status=HTTP_200_OK,
        )


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        serializer.save()

        username = serializer.data["username"]
        password = serializer.data["password"]

        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()

        token = Token.objects.create(user=user)

        return Response(
            {"token": token.key, "user": serializer.data},
            status=HTTP_201_CREATED,
        )


class ProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(instance=request.user)
        return Response(serializer.data, status=HTTP_200_OK)
