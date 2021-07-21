from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from board.models import Board, Post, Comment
from board.serializers import BoardSerializer, PostSerializer, CommentSerializer


class BoardViewset(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        comments_in_post = post.comments.all().order_by('-created_at')
        my_comment_in_post = post.comments.filter(creator=request.user, parent=None).order_by('-created_at').last()

        post_serializer = PostSerializer(post)
        comments_in_post_serialzier = CommentSerializer(comments_in_post, many=True)
        my_comment_in_post_serializer = CommentSerializer(my_comment_in_post)

        result = {
            "게시글": post_serializer.data,
            "해당 유저 댓글": my_comment_in_post_serializer.data,
            "해당게시글 전체 댓글": comments_in_post_serialzier.data
        }
        return Response(result, status=status.HTTP_200_OK)

    def perform_create(self, serializer):

        """
        perform_create()은 create()의 동작 중 일부분을 overriding한다고 생각하면 되는데,
        serializer.save()가 호출될 때 perform_create()가 호출된다고 생각하면 된다.
        perform_create()를 호출했지만, django에서는 개발자의 짐을 덜어주기위해 mixin으로 앞에서 설명한 list(), create()등을 제공하는 데,
        이때 자동으로 save()대신 perform_create()를 호출하는 것이다.
        """

        return serializer.save(creator=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        login_user = request.user
        instance = self.get_object()
        if instance.creator.username == login_user.username:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "작성자가 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        login_user = request.user
        instance = self.get_object()

        if instance.creator.username == login_user.username:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"msg": "작성자가 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(parent=None).order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    # def list(self, request, *args, **kwargs):
    #     user = self.request.user  # 로그인한 유저
    #
    #     board_detail_all_comment = Comment.objects.filter(post=1).order_by('-created_at')
    #
    #     # 로그인한 유저의 댓글중(자신의 댓글중 제일 마지막 댓글을 최상단에 보여지게끔 필터)
    #     personal_comment = Comment.objects.filter(creator=user.id, parent=None).order_by('created_at').last()
    #
    #     board_detail_all_comment_serializer = CommentSerializer(board_detail_all_comment, many=True)
    #     personal_comment_serializer = CommentSerializer(personal_comment)
    #
    #
    #     # board_detail_all_comment_serializer.is_valid(raise_exception=True)
    #     # personal_comment_serializer.is_valid(raise_exception=True)
    #
    #
    #     result = {"사용자 댓글": personal_comment_serializer.data,"나머지 댓글": board_detail_all_comment_serializer.data}
    #
    #     return Response(data=result, status=status.HTTP_200_OK)

    def perform_create(self, serializer):

        """
        perform_create()은 create()의 동작 중 일부분을 overriding한다고 생각하면 되는데,
        serializer.save()가 호출될 때 perform_create()가 호출된다고 생각하면 된다.
        perform_create()를 호출했지만, django에서는 개발자의 짐을 덜어주기위해 mixin으로 앞에서 설명한 list(), create()등을 제공하는 데,
        이때 자동으로 save()대신 perform_create()를 호출하는 것이다.
        """
        return serializer.save(creator=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        login_user = request.user
        instance = self.get_object()
        if instance.creator.username == login_user.username:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "작성자가 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        login_user = request.user
        instance = self.get_object()

        if instance.creator.username == login_user.username:
            self.perform_destroy(instance)
            return Response({"msg": "삭제 되었습니다"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"msg": "작성자가 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)