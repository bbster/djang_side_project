from django.test import TestCase
from board.models import Post, Board
from account.models import Auth


class BoardTest(TestCase):
    def setUp(self):
        self.user = Auth.objects.create_user(email="test@test.com", username="test", password="test")
        self.user2 = Auth.objects.create_user(email="test2@test.com", username="test2", password="test")
        self.board =Board.objects.create(type='notice')

    def _test_board_create(self):
        response = self.client.post("/account/login/", data={
            "email": "test@test.com",
            "password": "test"
        })
        response_json = response.json()

        response = self.client.post("/community/posts/", data={
            "board_type": self.board.id,
            "title": "test",
            "content": "test",
        })

        assert response.status_code == 201
        assert response.json()
        created_post_id = response.json()['id']

        post = Post.objects.get(id=created_post_id)
        assert post.creator and post.creator.email == 'test@test.com'
        assert post.creator_id == self.user.id

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

        self.client.post("/account/logout/")

        self.client.post("/account/login/", data={
            "email": "test2@test.com",
            "password": "test"
        })

        response = self.client.patch(f"/community/posts/{post_id}/",
                                   data={
                                       "board_type": self.board.id,
                                       "title": "test2",
                                       "content": "test2"},
                                   content_type='application/json')

        # response = self.client.put(f"/community/boards/{board_id}/",
        #                              data={
        #                                  "title": "test2",
        #                                  "text": "test2",
        #                                  "user": login_user.data['email']},
        #                              content_type='application/json')

        assert response.json() == {'msg': '작성자가 아닙니다.'}
        assert response.status_code == 400

    def test_board_update_garbage_data(self):
        post_response = self._test_board_create()  # 생성
        post_id = post_response.json()['id']

        print("board_response ::", post_response.data)

        response = self.client.patch(f"/community/boards/{post_id}/",
                                   data={
                                       "board_type": self.board.id,
                                       "title": "test2",
                                       "content": "add garbage data",
                                       "garbage": "nothing"},
                                   content_type='application/json')

        print("response.data ::", response.data)

        assert response.json()
        assert response.status_code == 200

    def test_board_delete(self):
        post_response = self._test_board_create()

        post_id = post_response.json()['id']

        response = self.client.delete(f"/community/posts/{post_id}/")

        assert response.status_code == 204

    def test_board_another_user_delete(self):
        post_response = self._test_board_create()

        post_id = post_response.json()['id']

        self.client.post("/account/logout/")

        self.client.post("/account/login/", data={
            "email": "test2@test.com",
            "password": "test"
        })

        response = self.client.delete(f"/community/posts/{post_id}/")

        assert response.json() == {"msg": "작성자가 아닙니다."}
        assert response.status_code == 400
