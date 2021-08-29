from unittest import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class TestWishListViewSet(TestCase):
    client = APIClient()

    def setUp(self):
        user = User.objects.create(username="testuser")
        user.set_password("12345")
        user.save()
        self.client.login(username="testuser", password="12345")

    def test_get_queryset(self):
        data = {"name": "test list 1"}
        response = self.client.post("/wish_list/", data, format='json')
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/wish_list/")
        self.assertEqual(response.status_code, 201)
        # self.fail()

    # def test_get_object(self):
    #     self.fail()
    #
    # def test_create(self):
    #     self.fail()
    #
    # def test_list(self):
    #     self.fail()
    #
    # def test_retrieve(self):
    #     self.fail()
    #
    # def test_partial_update(self):
    #     self.fail()
    #
    # def test_destroy(self):
    #     self.fail()
