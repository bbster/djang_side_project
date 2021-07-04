from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Users
from users.serializers import UserSerializer, SignUpSerializer


class UserList(APIView):
    def get(self, request):
        user_list = UserSerializer(Users.objects.all(), many=True)

        return Response(data=user_list.data, status=status.HTTP_200_OK)


class SignupView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(request.data)
        # if not serializer.is_valid():
        #     return Response(data=serializer.data, status=status.HTTP_400)

        user = Users.objects.create_user(username=serializer.data['username'], password=serializer.data['password'])
        user.save()
        token = Token.objects.create(user=user)

        return Response({"Token": token.key}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            token = Token.objects.filter(user=user)

            if not token: # 토큰값이 없다면 다시 생성
                token = Token.objects.create(user=user)
                return Response({"Token": token.key}, status=status.HTTP_200_OK)
            else: # 토큰값이 이미 있다면
                return Response({"Token": token.key}, status=status.HTTP_200_OK)

        else:
            return Response({"msg": "로그인 정보가 옳지 않습니다"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        # 로그인 되어 있는 token 값을 가져옴, db에 있는 토큰 값과 비교
        token = request.data['token']
        if token is not None:
            Token.objects.filter(key=token).delete()
            return Response({"msg": "로그아웃 되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "로그인이 되어 있지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
