from django import forms
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from service_objects.services import Service


class CheckingUniquenessEmailUser(Service):
    """Сервис для проверки на уникальность электронной почты во время регистрации"""

    user_email = forms.CharField()

    def process(self):
        user_email = self.cleaned_data["user_email"]
        User = get_user_model()
        try:
            user = User.objects.get(email=user_email)
        except:
            print("no")

        return Response("!")
