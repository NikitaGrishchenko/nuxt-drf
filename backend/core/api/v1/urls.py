from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("base/", include("apps.base.v1")),
]
