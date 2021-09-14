from apps.base.v1.views import (
    CheckUserTokenView,
    LoginView,
    LogoutView,
    UserInformationView,
    UserListView,
)

# from .views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "base"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/checking/", CheckUserTokenView.as_view(), name="user-check"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("user/info/", UserInformationView.as_view(), name="user-info"),
]
