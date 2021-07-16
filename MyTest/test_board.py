from django.test import TestCase
from board.models import Post, Board
from account.models import Auth


class BoardTest(TestCase):
    def setUp(self):
        self.user = Auth.objects.create_user(email="test@test.com", username="test", password="test")
        self.user2 = Auth.objects.create_user(email="test2@test.com", username="test2", password="test")
        self.board =Board.objects.create(type='notice')

    def _test_board_create(self):
        login_user = self.client.post("/account/login/", data={
            "email": "test@test.com",
            "password": "test"
        })

        response = self.client.post("/community/posts/", data={
            "board_type": self.board.id,
            "title": "test",
            "content": "test",
            "creator": self.user
        })

        assert response.status_code == 201
        assert response.json()

        return response

    def test_board_create(self):
        response = self._test_board_create()

        print("생성된 data", response.json())
        print("생성 status", response.status_code)

    def test_board_list(self):
        result = self._test_board_create()

        response = self.client.get("/community/posts/")

        print("리스트 data", response.json())
        print("리스트 status", response.status_code)

        assert response.status_code == 200
        assert response.json()

    def test_board_update(self):
        post_response = self._test_board_create()  # 생성
        post_id = post_response.json()['id']

        print("board_response ::", post_response.data)
        creator = post_response.data['creator']

        # response = self.client.put(f"/community/boards/{board_id}/",
        #                            data={
        #                                "title": "test2",
        #                                "text": "test2",
        #                                "user": creator},
        #                            content_type='application/json')

        response = self.client.patch(f"/community/posts/{post_id}/",
                                   data={
                                       "board_type": self.board.id,
                                       "title": "test2",
                                       "content": "test2",
                                       "creator": creator},
                                   content_type='application/json')

        assert response.json()
        assert response.status_code == 200

    def test_board_update_another_user(self):
        post_response = self._test_board_create()  # 생성
        post_id = post_response.json()['id']

        print("board_response ::", post_response.data)

        assert post_response.json()
        assert post_response.status_code == 201

        login_user = self.client.post("/account/login/", data={
            "email": "test2@test.com",
            "password": "test2"
        })

        assert login_user.json()
        assert login_user.status_code == 401

        # response = self.client.put(f"/community/boards/{board_id}/",
        #                              data={
        #                                  "title": "test2",
        #                                  "text": "test2",
        #                                  "user": login_user.data['email']},
        #                              content_type='application/json')

        # response = self.client.patch(f"/community/posts/{post_id}/",
        #                            data={
        #                                "board_type": self.board.id,
        #                                "title": "test2",
        #                                "content": "test2",
        #                                "creator": login_user.data['email']},
        #                            content_type='application/json')
        #
        # assert response.json()
        # assert response.status_code == 404



    def test_board_update_garbage_data(self):
        post_response = self._test_board_create()  # 생성
        post_id = post_response.json()['id']

        print("board_response ::", post_response.data)
        creator = post_response.data['creator']

        # response = self.client.put(f"/community/boards/{board_id}/",
        #                            data={
        #                                "title": "test2",
        #                                "text": "add garbage data",
        #                                "garbage": "nothing",
        #                                "user": creator},
        #                            content_type='application/json')

        response = self.client.patch(f"/community/boards/{post_id}/",
                                   data={
                                       "board_type": self.board.id,
                                       "title": "test2",
                                       "content": "add garbage data",
                                       "garbage": "nothing",
                                       "creator": creator},
                                   content_type='application/json')

        print("response.data ::", response.data)

        assert response.json()
        assert response.status_code == 200

    def test_board_delete(self):
        post_response = self._test_board_create()

        post_id = post_response.json()['id']

        response = self.client.delete(f"/community/posts/{post_id}/")
        assert response
