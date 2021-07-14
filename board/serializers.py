from rest_framework import serializers
from board.models import Boards, Comment


class BoardSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = Boards
        fields = ['id', 'title', 'creator', 'content', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ['id', 'board', 'creator', 'content', 'created_at', 'updated_at']
