from django.test import TestCase
from account.models import Auth


class SignupTest(TestCase):
    def test_signup(self):
        response = self.client.post("/account/signup/", data={
            "email": "test@test.com",
            "username": "tester",
            "password": "test"})

        assert response.status_code == 201
        assert response.json()
        print(response.status_code)
        print(response.json())


class LoginLogoutTest(TestCase):
    def setUp(self):
        self.user = Auth.objects.create_user(email="test@test.com", username="test", password="test")

    def test_login(self):

        response = self.client.post("/account/login/", data={"email": "test@test.com", "password": "test"})

        assert response.status_code == 200
        assert response.json()

        return response

    def test_logout(self):
        self.test_login()

        logout_response = self.client.post("/account/logout/")

        assert logout_response.status_code == 200
        assert logout_response.json()
        print(logout_response.status_code)
        print(logout_response.json())
