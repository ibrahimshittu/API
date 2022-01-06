from rest_framework import serializers
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
