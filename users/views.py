from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.models import Users
from users.serializers import UserSerializer


@api_view(['GET'])
def user_list(request):
    user_list = Users.objects.all()
    serializer = UserSerializer(user_list, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"msg": f"{username}님 로그인 되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "아이디 패스워드 정보가 옳지 않습니다. 다시 확인해주세요."},
                            status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({"msg": "POST 요청이 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)


def logout(request):
    if request.method == "POST":
        logout(request)
        return Response({"msg": "로그아웃 되었습니다."}, status=status.HTTP_200_OK)


def user_check(username):
    if Users.objects.get(username=username):
        return Response({"msg": f"{username}은 이미 존재하는 아이디입니다"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass


@api_view(['POST'])
def create_account(request):
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]
        user_check(username)
        user = Users.objects.create(username=username, password=password)
        user.save()
        login(request, user)
        return Response({"msg": f"{username} 회원이 생성되었습니다."}, status=status.HTTP_201_CREATED)




