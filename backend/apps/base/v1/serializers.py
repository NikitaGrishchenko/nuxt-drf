from apps.base.services import CreateUser
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserSerializer(ModelSerializer):
    """Сериализатор Пользователя"""

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "is_active"]


class UserCreateSerializer(ModelSerializer):
    """Создание нового пользователя"""

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        username_data = validated_data.pop("username")
        password_data = validated_data.pop("password")
        first_name_data = validated_data.pop("first_name")
        last_name_data = validated_data.pop("last_name")
        patronymic_data = validated_data.pop("patronymic")

        # Вызов сервиса - создание пользователя
        user = CreateUser.execute(
            {
                "username": username_data,
                "password": password_data,
                "first_name": first_name_data,
                "last_name": last_name_data,
                "patronymic": patronymic_data,
                "user_positions": user_positions_data,
            }
        )

        return user
