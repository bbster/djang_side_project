import json

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from comment.models import Comment
from comment.serializers import CommentSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = self.request.user  # 로그인한 유저

        all_comment = Comment.objects.filter(board=1).order_by('-created_at')

        # 로그인한 유저의 댓글중(자신의 댓글중 제일 마지막)
        personal_comment = Comment.objects.filter(board=1, user=user.id).order_by('created_at').last()

        all_comment_serializer = CommentSerializer(data=all_comment, many=True)
        personal_comment_serializer = CommentSerializer(data=personal_comment, many=True)

        result = {
            '사용자 댓글': personal_comment_serializer,
            '나머지 댓글': all_comment_serializer
        }

        return Response({"comments": result}, status=status.HTTP_200_OK)
