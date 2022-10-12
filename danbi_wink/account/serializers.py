from dataclasses import field
from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)


User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
        )
        try:
            validate_password(validated_data['password'])
            user.set_password(validated_data['password'])
            user.save()
            return user
        except Exception as e:
            raise ValidationError(e)


    class Meta:
        model = User
        fields = ['name', 'email', 'password']
