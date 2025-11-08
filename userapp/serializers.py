from typing import Any

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserSerializer(serializers.ModelSerializer):
    refresh_token = serializers.CharField(read_only=True)
    access_token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
            "refresh_token",
            "access_token",
        ]
        extra_kwargs = {
            "email": {"write_only": True},
            "username": {"write_only": True},
            "password": {"write_only": True},
            "phone": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = True
        user.save()
        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token
        return {"refresh_token": refresh_token, "access_token": access_token}


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(username=email, password=password)

        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            return {
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
                "user": user,
            }
        raise serializers.ValidationError("Invalid email or password")


class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    access_token = serializers.CharField(read_only=True)
    extra_kwargs = {
        "refresh_token": {"write_only": True},
    }
    def validate(self, data):
        refresh_token = data.get("refresh_token")
        try:
            refresh = RefreshToken(refresh_token)
            return {
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            }
        except Exception as e:
            raise serializers.ValidationError("Invalid refresh token") from e
        


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            'avatar',
        ]
        extra_kwargs = {
            "email": {"required": False},
            "first_name": {"required": False},
            "last_name": {"required": False},
            "phone_number": {"required": False},
            "avatar": {"required": False},
        }
