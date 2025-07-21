from django.db import models
from django.db.models.base import Model
from rest_framework import fields, serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import serializers
# from . import google
# from .register import register_social_user
import os
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters',
        'email': 'Email must be a tradebrains.in email'
    }

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'employee_name', 'reporting_manager', 'designation']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError({'username': self.default_error_messages['username']})

        if not email.lower().endswith('@tradebrains.in'):
            raise serializers.ValidationError({'email': self.default_error_messages['email']})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_verified = True  # Automatically verified
        user.save()
        return user



class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens', 'is_superuser']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

        if user.auth_provider != 'email':
            raise AuthenticationFailed(f'Please continue your login using {user.auth_provider}')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens(),
            'user_id': user.id,
            'is_superuser': user.is_superuser
        }
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'employee_name', 'reporting_manager', 'designation']

