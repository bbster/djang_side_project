from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Users


class SignupView(APIView):
    def post(self, request):
        user = Users.objects.create_user(email=request.data['email'], username=request.data['username'],
                                         password=request.data['password'])

        user.save()
        token = Token.objects.create(user=user)
        return Response({"Token": token.key}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        print(request.data.get['username'])
        print(request.data['password'])
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        print("user:", user)
        if user is not None:
            token = Token.objects.create(user=user)
            return Response({"Token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "로그인 정보가 옳지 않습니다"}, status=status.HTTP_401_UNAUTHORIZED)
