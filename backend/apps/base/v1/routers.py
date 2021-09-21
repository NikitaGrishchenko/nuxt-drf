from apps.base.v1.views import (
    CheckUserTokenView,
    LoginView,
    LogoutView,
    UserInformationView,
    UserListView,
)
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
    # user
    path("user/info/", UserInformationView.as_view(), name="user-info"),
    path("user/check/", CheckUserTokenView.as_view(), name="user-check"),
    path("user/list/", UserListView.as_view(), name="user-list"),
]
