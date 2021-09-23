from django import forms
from django.contrib.auth import get_user_model
from service_objects.services import Service


class CreateUser(Service):
    """Сервис для создания пользователя"""

    username = forms.CharField()
    password = forms.CharField()

    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField(required=False)

    def process(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        patronymic = self.cleaned_data["patronymic"]

        User = get_user_model()
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        if patronymic:
            user.patronymic = patronymic
        user.save()

        return user
