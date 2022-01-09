from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestSetup(APITestCase):
    def setUp(self):

        fake = Faker()

        self.register_url = reverse('register')
        self.login = reverse('login')

        self.user_data = {
            'email': fake.email(),
            'username': fake.email().split('@')[0],
            'password': fake.email()
        }

        return super().setUp()

    def tearDown(self):

        return super().tearDown()
