from django.test import TestCase
from users.models import Users


class SignupTest(TestCase):
    def test_signup(self):
        response = self.client.post("/users/signup/", data={
            "username": "test",
            "password": "test"})

        assert response.status_code == 201
        assert response.json()
        print(response.status_code)
        print(response.json())


class LoginLogoutTest(TestCase):
    def setUp(self):
        self.user = Users.objects.create_user(username="test", password="test")

    def test_login(self):
        response = self.client.post("/users/login/", data={
            "username": "test",
            "password": "test"
        })

        assert response.status_code == 200
        assert response.json()

        return response

    def test_logout(self):
        response = self.test_login()

        logout_response = self.client.post("/users/logout/", data=response.json())

        assert logout_response.status_code == 200
        assert logout_response.json()
        print(logout_response.status_code)
        print(logout_response.json())
