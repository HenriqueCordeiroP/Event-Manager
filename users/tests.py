from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class ListUsersTests(APITestCase):
    url = "/api/v1/users/"

    def setUp(self):
        self.user = User.objects.create(
            email="test@user.com",
            name="test",
            password="testpass",
            date_of_birth="2000-01-01",
        )

        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        User.objects.all().delete()
        return super().tearDown()

    def test_unauthorized(self):
        self.client.logout()

        response = self.client.get(self.url, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_one_user(self):

        response = self.client.get(self.url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            [
                {
                    "id": str(self.user.id),
                    "email": "test@user.com",
                    "name": "test",
                    "date_of_birth": "2000-01-01",
                }
            ],
        )

    def test_many_user(self):
        user2 = User.objects.create(
            email="test2@user.com",
            name="test2",
            password="testpass",
            date_of_birth="2000-01-01",
        )

        response = self.client.get(self.url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            [
                {
                    "id": str(self.user.id),
                    "email": "test@user.com",
                    "name": "test",
                    "date_of_birth": "2000-01-01",
                },
                {
                    "id": str(user2.id),
                    "email": "test2@user.com",
                    "name": "test2",
                    "date_of_birth": "2000-01-01",
                },
            ],
        )


class GetUserTests(APITestCase):
    base_url = "/api/v1/users/"
    url = ""

    def setUp(self):
        self.user = User.objects.create(
            email="test@user.com",
            name="test",
            password="testpass",
            date_of_birth="2000-01-01",
        )

        self.url = f"{self.base_url}{self.user.id}"
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        User.objects.all().delete()
        return super().tearDown()

    def test_unauthorized(self):
        self.client.logout()

        response = self.client.get(self.url, format="json", follow=True)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user(self):

        response = self.client.get(self.url, format="json", follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": str(self.user.id),
                "email": "test@user.com",
                "name": "test",
                "date_of_birth": "2000-01-01",
            },
        )

    def test_get_other_user(self):
        user2 = User.objects.create(
            email="test2@user.com",
            name="test2",
            password="testpass",
            date_of_birth="2000-01-01",
        )

        response = self.client.get(
            f"{self.base_url}{user2.id}", format="json", follow=True
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": str(user2.id),
                "email": "test2@user.com",
                "name": "test2",
                "date_of_birth": "2000-01-01",
            },
        )
