from .test_setup import TestSetup
from rest_framework import status
from ..models import User


class Test_view(TestSetup):
    def test_user_can_create_account(self):

        response = self.client.post(
            self.register_url, self.user_data, format='json')

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)
        self.assertEqual(response.data['details']
                         ['email'], self.user_data['email'])

    def test_user_cannot_login_unverified(self):

        response = self.client.post(
            self.register_url, self.user_data, format='json')
        response = self.client.post(
            self.login, self.user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_can_login_verified(self):

        response = self.client.post(
            self.register_url, self.user_data, format='json')

        user = User.objects.get(email=self.user_data['email'])
        user.is_verified = True
        user.save()

        response = self.client.post(
            self.login, self.user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
