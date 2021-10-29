from apps.base.services import CreateUser
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserSerializer(ModelSerializer):
    """Сериализатор Пользователя"""

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "is_active"]


class UserCreateSerializer(ModelSerializer):
    """Создание нового пользователя"""

    password_confirmation = serializers.CharField(
        write_only=True, max_length=100
    )

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "password_confirmation",
        ]

    def create(self, validated_data):
        email_data = validated_data.pop("email")
        password_data = validated_data.pop("password")
        first_name_data = validated_data.pop("first_name")
        last_name_data = validated_data.pop("last_name")
        password_confirmation_data = validated_data.pop(
            "password_confirmation"
        )

        # Вызов сервиса - создание пользователя
        return CreateUser.execute(
            {
                "email": email_data,
                "password": password_data,
                "first_name": first_name_data,
                "last_name": last_name_data,
                "password_confirmation": password_confirmation_data,
            }
        )
