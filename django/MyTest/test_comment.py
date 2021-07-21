from django.test import TestCase
from board.models import Board, Post, Comment
from account.models import Auth


class CommentTest(TestCase):
    def setUp(self):
        Auth.objects.create_user(email="test@test.com", username="test", password="test")
        Auth.objects.create_user(email="test2@test.com", username="test2", password="test")
        self.board = Board.objects.create(type='notice')

    def _test_comment_create(self):
        self.client.post("/account/login/", data={
            "email": "test@test.com",
            "password": "test"
        })

        self.client.post("/community/posts/", data={
            "board_type": self.board.id,
            "title": "test",
            "content": "test",
        })

        response = self.client.post("/community/comments/", data={
            "content": "create Comment_test"
        })

        return response

    # 생성
    def test_comment_create(self):
        self._test_comment_create()

        comment_response = self.client.post("/community/comments/", data={
            "content": "create comment in comment test"
        })

        response = self.client.post("/community/comments/", data={
            "parent": comment_response.json()['id'],
            "content": "comment in comment"
        })

        assert response.json()
        assert response.status_code == 201

    # 댓글 생성시 로그인 유저 값 말고 임의 유저이름값 넣어봤을때
    def test_comment_dummy_user_name_create(self):
        self._test_comment_create()

        comment_response = self.client.post("/community/comments/", data={
            "content": "create comment in comment test",
            "creator": "dummy_user"
        })

        print("comment_response_creator::", comment_response.json()['creator'])

        response = self.client.post("/community/comments/", data={
            "parent": comment_response.json()['id'],
            "content": "comment in comment",
            "creator": "dummy_user"
        })

        print("creator::", response.json()['creator'])
        assert response.json()
        assert response.status_code == 201

    # 특수기호
    def test_special_symbol_create(self):
        self._test_comment_create()

        response = self.client.post("/community/comments/", data={
            "content": "!@#$%^&*()_+}{|?><:;'|sadf'asd",
        })

        print("comment_response_creator::", response.json()['creator'])

        assert response.json()
        assert response.status_code == 201

    # 리스트
    def test_comment_list(self):
        self._test_comment_create()

        response = self.client.get("/community/comments/")

        assert response.json()
        assert response.status_code == 200

        print(response.json())
        print(response.status_code)

    # 수정
    def test_comment_update(self):
        response_comment = self._test_comment_create()

        response = self.client.put(f"/community/comments/{response_comment.json()['id']}/",
                                   data={
                                       "content": "change Comments"
                                   }, content_type='application/json')

        assert response.json()
        assert response.status_code == 200

    # 수정 creator에 임의 유저값 넣어봤을때
    def test_comment_dummy_user_update(self):
        response_comment = self._test_comment_create()

        response = self.client.put(f"/community/comments/{response_comment.json()['id']}/",
                                   data={
                                       "content": "change Comments",
                                       "creator": "dummy_user"
                                   }, content_type='application/json')

        print(f"change user? :: {response.json()['creator']}")
        assert response.json()
        assert response.status_code == 200

    # 수정 id값 임의로 넣어봄
    def test_comment_dummy_index_value_update(self):
        response_comment = self._test_comment_create()

        response = self.client.put(f"/community/comments/{response_comment.json()['id']}/",
                                   data={
                                       "id": 60,
                                       "content": "change Comments",
                                   }, content_type='application/json')

        print(f"\nchange id? :: {response_comment.data['id']}\n")
        print(f"change id? :: {response_comment.data['content']}\n")
        print(f"change id? :: {response.json()['id']}\n")
        print(f"change id? :: {response.json()['content']}")
        assert response.json()
        assert response.status_code == 200

    # 삭제
    def test_comment_delete(self):
        response_comment = self._test_comment_create()

        print("삭제전", Comment.objects.all())

        response = self.client.delete(f"/community/comments/{response_comment.json()['id']}/")
        print("삭제후", Comment.objects.all())

        assert response.status_code == 204

    # 삭제 작성자가 아닌 다른 유저가 삭제 요청
    def test_comment_another_user_delete(self):
        response_comment = self._test_comment_create()

        print(f"\n삭제전 {Comment.objects.all()}\n")
        self.client.post("/account/logout/")

        self.client.post("/account/login/", data={
            "email": "test2@test.com",
            "password": "test"
        })

        response = self.client.delete(f"/community/comments/{response_comment.json()['id']}/")
        print(f"삭제후 :: {Comment.objects.all()}")

        assert response.json() == {'msg': '작성자가 아닙니다.'}
        assert response.status_code == 400
