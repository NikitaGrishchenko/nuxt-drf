
from apps.base.v1.views import LoginView, RefreshView, UserListView
# from .views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "base"

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view(), name="login"),
    path('refresh/', RefreshView.as_view(), name="refresh")
]
