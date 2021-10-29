from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from service_objects.services import Service


class CheckingUniquenessEmailUser(Service):
    """Сервис для проверки на уникальность электронной почты во время
    регистрации, возвращает в data {success: true} - если email уникальный,
    и {success: false} - если такой email уже существует в базе данных """

    user_email = forms.CharField()

    def process(self):
        user_email = self.cleaned_data["user_email"]
        users = get_user_model()

        try:
            user = users.objects.get(email=user_email)
            if user:
                content = {"success": False}
                return Response(content)
        except ObjectDoesNotExist:
            content = {"success": True}
            return Response(content)
