from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import (
    BaseUserManager,
    Group,
    PermissionsMixin,
    UserManager,
)
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        _("username"),
        max_length=30,
        unique=True,
    )
    email = models.CharField(
        verbose_name=("E-mail"), max_length=60, unique=True
    )
    first_name = models.CharField(verbose_name=("Имя"), max_length=40)
    last_name = models.CharField(
        verbose_name=("Фамилия"), max_length=30, blank=True, null=True
    )
    date_of_birth = models.DateField(
        verbose_name=("Дата рождения"), blank=True, null=True
    )
    photo = models.ImageField(
        verbose_name=("Аватарка"),
        upload_to="photo/",
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpeg", "jpg", "png"])
        ],
    )
    is_active = models.BooleanField(_("active"), default=False)
    date_joined = models.DateTimeField(
        verbose_name=("Дата создания"), default=timezone.now
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
    )

    objects = UserManager()

    # EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"

    class Meta:
        swappable = "AUTH_USER_MODEL"
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
        ordering = ("-date_joined",)

    def __str__(self):
        return self.username
