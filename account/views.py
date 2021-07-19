from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Auth
from account.serializers import UserSerializer, SignUpSerializer, LoginSerializer


class UserList(APIView):
    def get(self, request):
        user_list = UserSerializer(Auth.objects.all(), many=True)

        return Response(data=user_list.data, status=status.HTTP_200_OK)


class SignupView(APIView):
    # 회원 가입시 username은 email 형태로
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"msg": "serializer.is_valid error"}, status=status.HTTP_400_BAD_REQUEST)

        user = Auth.objects.create_user(email=serializer.data['email'], username=serializer.data['username'], password=serializer.data['password'])

        # email = EmailMessage('Email test', 'email 발송 테스트', to=[serializer.data['username']])
        # email.send()

        user.save()

        # token = Token.objects.create(user=user)
        return Response(f"{serializer.data['username']}님 회원가입을 축하합니다.", status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = authenticate(email=serializer.data['email'], password=serializer.data['password'])

            if user is not None:
                login(request, user)
                login_username = Auth.objects.get(email=serializer.data['email'])
                data = {
                    'msg': f"{login_username}님 환영합니다.",
                }
                return Response(data, status=status.HTTP_200_OK)

                # token = Token.objects.filter(user=user)
                # if not token:  # 토큰값이 없다면 다시 생성
                #     token = Token.objects.create(user=user)
                #     return Response({"token": token.key}, status=status.HTTP_200_OK)
                # else:  # 토큰값이 이미 있다면
                #     login(request, user)
                #     return Response({"token": token.key}, status=status.HTTP_200_OK)
            else:
                return Response({"msg": "로그인 정보가 없습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response({"msg": "로그인 정보가 옳지 않습니다"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        user = self.request.user
        if user is not None:
            logout(request)
            return Response({"msg": "로그아웃 되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "로그인 되어 있지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

        # token = request.data['token']
        # if token is not None:
        #     Token.objects.get(key=token).delete()
        #     return Response({"msg": "로그아웃 되었습니다."}, status=status.HTTP_200_OK)
        # else:
        #     return Response({"msg": "로그인이 되어 있지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
