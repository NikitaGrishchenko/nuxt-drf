
import os

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Overriding the command to create an application'


    def add_arguments(self, parser):
        parser.add_argument(
            "name", type=str, help="Name of the application or project"
        )

    def handle(self, *args, **options):
        name = options["name"]
        path_to_folder = os.path.join(settings.APPS_DIR)
        path = os.path.join(path_to_folder, name)
        template = settings.APP_TEMPLATE
        if not os.path.exists(path):
            os.mkdir(path)
        management.call_command(
            "startapp", name, path, f"--template={template}"
        )
