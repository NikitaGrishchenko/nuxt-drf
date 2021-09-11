from django.contrib.auth import get_user_model
from rest_framework import exceptions, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as BaseTokenObtainPairSerializer,
)
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer as BaseTokenRefreshSerializer,
)
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    """Сериализатор токена доступа"""

    @classmethod
    def get_extra_keys(cls, user):
        """Получить дополнительные поля для payload токена

        Аргументы:
            user - пользователь
        """

        return {
            "id": user.id,
            "username": user.username,
        }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token.payload.update(cls.get_extra_keys(user))
        return token


class TokenRefreshSerializer(BaseTokenRefreshSerializer):
    """Сериализатор токена обновления"""

    def get_user_info(self, user_id):
        """Получить актуальную информацию о пользователе

        Аргументы:
            user_id - идентификатор пользователя
        """

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("Пользователь не найден")

        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                "Пользователь не активирован"
            )

        return TokenObtainPairSerializer.get_extra_keys(user)

    def validate(self, attrs):
        refresh = RefreshToken(attrs["refresh"])
        user_id = refresh.payload["user_id"]

        # обновляем payload токенов
        refresh.payload.update(self.get_user_info(user_id))

        data = {"access": str(refresh.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()

            data["refresh"] = str(refresh)

        return data


class UserListSerializer(ModelSerializer):
    """Список пользователей"""

    class Meta:
        model = User
        fields = "__all__"
