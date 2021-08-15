from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ApiConfig(AppConfig):
    """Default app config"""

    name = "core.api"
    verbose_name = _("Api")
