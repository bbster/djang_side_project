from django.test import TestCase
from boards.models import Boards
from users.models import Users


class BoardTest(TestCase):
    def setUp(self):
        self.user = Users.objects.create_user(username="test", password="test")
        self.user2 = Users.objects.create_user(username="test2", password="test2")

    def _test_board_create(self):
        login_user = self.client.post("/users/login/", data={
            "username": "test",
            "password": "test"
        })

        response = self.client.post("/comunity/boards/", data={
            "title": "test",
            "text": "test",
            "user": login_user
        })

        assert response.status_code == 201
        assert response.json()

        return response

    def test_board_create(self):
        response = self._test_board_create()
        print("생성된 data", response.json())
        print("생성 status", response.status_code)

    def test_board_list(self):
        self._test_board_create()
        response = self.client.get("/comunity/boards/")

        print("리스트 data", response.json())
        print("리스트 status", response.status_code)

        assert response.status_code == 200
        assert response.json()

    def test_board_delete(self):
        board_response = self._test_board_create()
        print(Boards.objects.all())
        board_id = board_response.json()['id']

        response = self.client.delete(f"/comunity/boards/{board_id}/")
        print(Boards.objects.all())
        breakpoint()
        print("삭제", )

        assert response
