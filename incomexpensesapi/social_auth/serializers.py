from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from . import google, register
import os


class GoogleAuthViewSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    class Meta:
        fields = ['auth_token']

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):

            raise AuthenticationFailed('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register.register_social_user(
            provider=provider, user_id=user_id, email=email, name=name)
