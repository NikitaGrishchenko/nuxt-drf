# from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenCookieDeleteView,
#     TokenVerifyView,
# )

from apps.base.v1.views import UserListView

# from .views import TokenObtainPairView, TokenRefreshView
from django.urls import path

app_name = "base"

urlpatterns = [
    path("test/", UserListView.as_view(), name="user-list"),
    # path(
    #     "token/",
    #     TokenObtainPairView.as_view(
    #         token_refresh_view_name="api:v1:auth:token_refresh"
    #     ),
    #     name="token_obtain_pair",
    # ),
    # path(
    #     "refresh/",
    #     TokenRefreshView.as_view(
    #         token_refresh_view_name="api:v1:auth:token_refresh"
    #     ),
    #     name="token_refresh",
    # ),
    # path("verify/", TokenVerifyView.as_view(), name="token_verify"),
    # path(
    #     "delete/",
    #     TokenCookieDeleteView.as_view(
    #         token_refresh_view_name="api:v1:auth:token_refresh"
    #     ),
    #     name="token_delete",
    # ),
]
