from rest_framework import serializers
from users.models import Users


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users

        fields = (
            'id',
            'username',
            'password',
        )


# TODO 기능별 serializer 추가해보기
class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True)