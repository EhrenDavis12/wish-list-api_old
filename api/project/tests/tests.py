from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from api.project.models import Item


class ItemTestCase(TestCase):
    client = APIClient()

    def setUp(self):
        # self.credentials = {"username": "testuser", "password": "secret"}
        # self.client.user = User.objects.create_user(**self.credentials)
        # self.client.post("/login/", self.credentials, follow=True)

        user = User.objects.create(username="testuser")
        user.set_password("12345")
        user.save()
        # self.client = Client()
        self.client.login(username="testuser", password="12345")

        # response = self.client.get("/account/profile/{}/".format(user.id), follow=True)
        # self.assertEqual(response.status_code, 200)
        # Item.objects.create(name="New Item")

    def test_wish_list(self):
        """Items that can speak are correctly identified"""
        data = {"name": "test list 1"}
        response = self.client.post("/wish_list/", data, format='json')
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/wish_list/")
        self.assertEqual(response.status_code, 200)
        # item = Item.objects.get(name="New Item")
        # self.assertEqual(item.name(), "New Item")

