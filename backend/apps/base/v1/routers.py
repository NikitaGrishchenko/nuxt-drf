
from apps.base.v1.views import UserListView
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
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
