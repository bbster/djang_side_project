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

    def test_board_update(self):
        board_response = self._test_board_create()  # 생성
        board_id = board_response.json()['id']

        print("board_response ::", board_response.data)
        creator = board_response.data['user']

        # response = self.client.put(f"/comunity/boards/{board_id}/",
        #                            data={
        #                                "title": "test2",
        #                                "text": "test2",
        #                                "user": creator},
        #                            content_type='application/json')

        response = self.client.patch(f"/comunity/boards/{board_id}/",
                                   data={
                                       "title": "test2",
                                       "text": "test2",
                                       "user": creator},
                                   content_type='application/json')

        assert response.json()
        assert response.status_code == 200

    def test_board_update_another_user(self):
        board_response = self._test_board_create()  # 생성
        board_id = board_response.json()['id']

        print("board_response ::", board_response.data)

        login_user = self.client.post("/users/login/", data={
            "username": "test2",
            "password": "test2"
        })

        # response = self.client.put(f"/comunity/boards/{board_id}/",
        #                              data={
        #                                  "title": "test2",
        #                                  "text": "test2",
        #                                  "user": login_user.data['username']},
        #                              content_type='application/json')

        response = self.client.patch(f"/comunity/boards/{board_id}/",
                                   data={
                                       "title": "test2",
                                       "text": "test2",
                                       "user": login_user.data['username']},
                                   content_type='application/json')
        assert response.json()
        assert response.status_code == 400

    def test_board_update_garbage_data(self):
        board_response = self._test_board_create()  # 생성
        board_id = board_response.json()['id']

        print("board_response ::", board_response.data)
        creator = board_response.data['user']

        # response = self.client.put(f"/comunity/boards/{board_id}/",
        #                            data={
        #                                "title": "test2",
        #                                "text": "add garbage data",
        #                                "garbage": "nothing",
        #                                "user": creator},
        #                            content_type='application/json')

        response = self.client.patch(f"/comunity/boards/{board_id}/",
                                   data={
                                       "title": "test2",
                                       "text": "add garbage data",
                                       "garbage": "nothing",
                                       "user": creator},
                                   content_type='application/json')

        print("response.data ::", response.data)

        assert response.json()
        assert response.status_code == 200

    def test_board_delete(self):
        board_response = self._test_board_create()

        board_id = board_response.json()['id']

        response = self.client.delete(f"/comunity/boards/{board_id}/")
        assert response
