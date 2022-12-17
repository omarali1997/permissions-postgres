from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Snack


from django.urls import reverse


class SnackTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_snack = Snack.objects.create(
            title="rake",
            purchaser=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_snack.save()

    def setUp(self):
        self.client.login(username='testuser1', password="pass")

    def test_Snack_model(self):
        snack = Snack.objects.get(id=1)
        actual_purchaser = str(snack.purchaser)
        actual_name = str(snack.title)
        actual_description = str(snack.description)
        self.assertEqual(actual_purchaser, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_snack_list(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Snack = response.data
        self.assertEqual(len(Snack), 1)

    def test_auth_required(self):
        self.client.logout()
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("snack_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
