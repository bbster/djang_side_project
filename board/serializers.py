from rest_framework import serializers
from board.models import Board, Post, Comment


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'type']


class PostSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['id', 'board_type', 'title', 'creator', 'content', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'creator', 'content', 'created_at', 'updated_at']
