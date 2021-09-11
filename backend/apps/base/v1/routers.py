from apps.base.v1.views import LoginView, UserListView

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
    path("users/", UserListView.as_view(), name="user-list"),
]
