from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    """Command create default superuser"""

    help = "Create default superuser"

    def handle(self, *args, **options):
        if (
            settings.ADMIN_USERNAME
            and settings.ADMIN_EMAIL
            and settings.ADMIN_PASSWORD
        ):
            try:
                user = User.objects.get(username=settings.ADMIN_USERNAME)
                user.is_superuser = True
                user.is_staff = True
                user.email = settings.ADMIN_EMAIL
                user.set_password(settings.ADMIN_PASSWORD)
                user.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f"  • User {settings.ADMIN_USERNAME} updated"
                    )
                )
            except User.DoesNotExist:
                User.objects.create_user(
                    username=settings.ADMIN_USERNAME,
                    email=settings.ADMIN_EMAIL,
                    password=settings.ADMIN_PASSWORD,
                    is_superuser=True,
                    is_staff=True,
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"  • User {settings.ADMIN_USERNAME} created"
                    )
                )
