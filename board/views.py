from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from board.models import Boards
from board.serializers import BoardSerializer


class BoardViewset(viewsets.ModelViewSet):
    queryset = Boards.objects.all().order_by('-created_at')
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        """
        perform_create()은 create()의 동작 중 일부분을 overriding한다고 생각하면 되는데,
        serializer.save()가 호출될 때 perform_create()가 호출된다고 생각하면 된다.
        perform_create()를 호출했지만, django에서는 개발자의 짐을 덜어주기위해 mixin으로 앞에서 설명한 list(), create()등을 제공하는 데,
        이때 자동으로 save()대신 perform_create()를 호출하는 것이다.
        """
        return serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        login_user = request.user
        instance = self.get_object()
        if instance.user.username == login_user.username:
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

        if instance.user.username == login_user.username:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"msg": "작성자가 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)

