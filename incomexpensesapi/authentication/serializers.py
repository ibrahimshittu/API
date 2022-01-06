from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from .models import User


class registerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True, max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should be alphanumeric')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class emailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True, max_length=555, min_length=6)

    class Meta:
        model = User
        fields = ['token']


class loginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=256, min_length=5)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=68, min_length=6, read_only=True)
    tokens = serializers.CharField(
        max_length=268, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed(
                'Yo! Invalid credentials, check again')

        if not user.is_verified:
            raise AuthenticationFailed(
                'Chill, Verify your account fess')

        if not user.is_active:
            raise AuthenticationFailed(
                'we don lock your account, contact us!')

        return {
            "email": user.email,
            "username": user.username,
            "tokens":  user.tokens
        }
