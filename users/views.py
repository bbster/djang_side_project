from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Users
from users.serializers import UserSerializer


class UserList(APIView):
    def get(self, request):
        user_list = UserSerializer(Users.objects.all(), many=True)

        return Response(data=user_list.data, status=status.HTTP_200_OK)


class SignupView(APIView):
    def post(self, request):
        user = Users.objects.create_user(username=request.data['username'], password=request.data['password'])

        user.save()
        token = Token.objects.create(user=user)
        return Response({"Token": token.key}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            token = Token.objects.get(user=user)

            if token is not None: # 토큰값이 이미 있다면
                return Response({"Token": token.key}, status=status.HTTP_200_OK)
            else: # 토큰값이 없다면 다시 생성
                token = Token.objects.create(user=user)
                return Response({"Token": token.key}, status=status.HTTP_200_OK)

        else:
            return Response({"msg": "로그인 정보가 옳지 않습니다"}, status=status.HTTP_401_UNAUTHORIZED)


# class LogOut(APIView):
#     def post(self, request):
#         username = request.