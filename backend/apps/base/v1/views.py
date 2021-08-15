# from apps.base.models import User
from apps.base.v1.serializers import UserListSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView


class UserListView(ListCreateAPIView):
    """Вывод пользователей"""

    serializer_class = UserListSerializer
    User = get_user_model()
    queryset = User.objects.all()


# from rest_framework_simplejwt.views import (
#     TokenObtainPairView as BaseTokenObtainPairView,
# )
# from rest_framework_simplejwt.views import (
#     TokenRefreshView as BaseTokenRefreshView,
# )

# from .serializers import TokenObtainPairSerializer, TokenRefreshSerializer


# class TokenObtainPairView(BaseTokenObtainPairView):
#     """Представление для получения токена доступа"""

#     serializer_class = TokenObtainPairSerializer


# class TokenRefreshView(BaseTokenRefreshView):
#     """Представление для обновления токена доступа"""

#     serializer_class = TokenRefreshSerializer
