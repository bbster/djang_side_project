from rest_framework import serializers
from account.models import Auth


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auth

        fields = (
            'id',
            'email',
            'username',
            'password',
        )


# TODO 기능별 serializer 추가해보기
class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
