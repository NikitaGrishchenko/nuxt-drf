import datetime

from apps.base.services import (
    CheckingUniquenessEmailUser,
    GetUserCookieHttponly,
)
from apps.base.v1.serializers import UserCreateSerializer, UserSerializer
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserEmailCheckView(APIView):
    """Проверка на уникальность электронной почты во время регистрации"""

    permission_classes = [AllowAny]

    def post(self, request, format=None):
        user_email = request.data["email"]
        return CheckingUniquenessEmailUser.execute({"user_email": user_email})


class CheckUserTokenView(APIView):
    """Проверка действительности токена доступа"""

    def get(self, request, format=None):
        return HttpResponse(status=200)


class UserInformationView(APIView):
    """Информация о авторизированном пользователе"""

    def get(self, request, format=None):
        if request.COOKIES[settings.SIMPLE_JWT["AUTH_COOKIE"]]:
            token = request.COOKIES[settings.SIMPLE_JWT["AUTH_COOKIE"]]
            user = GetUserCookieHttponly.execute({"token": token})
        return Response(user.data)


class UserListView(ListCreateAPIView):
    """Вывод пользователей"""

    serializer_class = UserSerializer
    User = get_user_model()
    queryset = User.objects.all()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class LogoutView(APIView):
    """Представление для удаления токена доступа JWT в cookie с флагом httpOnly"""

    def post(self, request, format=None):
        response = Response()

        response.set_cookie(
            key=settings.SIMPLE_JWT["AUTH_COOKIE"],
            value=None,
            expires=0,
        )

        response.data = {
            "Success": "Logout successfully",
        }
        return response


class LoginView(APIView):
    """Представление для сохранения токена доступа JWT в cookie с флагом httpOnly"""

    # отключение проверки подлинности токена
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        data = request.data
        response = Response()
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)

                # user_id = user.id

                response.set_cookie(
                    key=settings.SIMPLE_JWT["AUTH_COOKIE"],
                    value=data["access"],
                    # expires=datetime.datetime.utcnow()
                    # + settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                    # secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                    # httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                    # samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
                )

                # csrf.get_token(request)
                response.data = {
                    "Success": "Login successfully",
                    # "user_id": user_id,
                }
                return response
            else:
                return Response(
                    {"No active": "This account is not active!!"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"Invalid": "Invalid username or password!!"},
                status=status.HTTP_404_NOT_FOUND,
            )


class UserCreateView(ListCreateAPIView):
    """Список и создание пользователя"""

    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
