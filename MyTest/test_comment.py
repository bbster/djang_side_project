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

        response = self.client.post("/community/comments/", data={
            "content": "create Comment_test"
        })

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

    # 삭제
    def test_comment_delete(self):
        response_comment = self._test_comment_create()

        print("삭제전", Comment.objects.all())

        response = self.client.delete(f"/community/comments/{response_comment.json()['id']}/")
        print("삭제후", Comment.objects.all())

        assert response.status_code == 204
