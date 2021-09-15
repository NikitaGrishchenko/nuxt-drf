from django.urls import include, path

from .views import SchemaView

app_name = "api"

urlpatterns = [
    path(
        "",
        SchemaView.with_ui("swagger", cache_timeout=0),
        name="documentation",
    ),
    path("v1/", include("core.api.v1")),
]
