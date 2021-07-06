from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from boards.models import Boards
from boards.serializers import BoardSerializer


class BoardViewset(viewsets.ModelViewSet):
    queryset = Boards.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):

        """
        perform_create()은 create()의 동작 중 일부분을 overriding한다고 생각하면 되는데,
        serializer.save()가 호출될 때 perform_create()가 호출된다고 생각하면 된다.
        perform_create()를 호출했지만, django에서는 개발자의 짐을 덜어주기위해 mixin으로 앞에서 설명한 list(), create()등을 제공하는 데,
        이때 자동으로 save()대신 perform_create()를 호출하는 것이다.

        """
        breakpoint()
        return serializer.save(user=self.request.user)

    # def list(self, request):
    #     pass
    #
    # def create(self, request):
    #     pass
    #
    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
    #
    # def destroy(self, request, pk=None):
    #     pass
