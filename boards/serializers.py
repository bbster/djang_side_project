from rest_framework import serializers
from boards.models import Boards


class BoardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Boards
        fields = ['id', 'title', 'user', 'content', 'created_at', 'updated_at']
