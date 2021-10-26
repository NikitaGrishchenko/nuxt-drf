from django import forms
from django.contrib.auth import get_user_model
from service_objects.services import Service


class CreateUser(Service):
    """Сервис для создания пользователя"""

    email = forms.CharField()
    password = forms.CharField()
    password_confirmation = forms.CharField()

    first_name = forms.CharField()
    last_name = forms.CharField()
    # patronymic = forms.CharField(required=False)

    def process(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        password_confirmation = self.cleaned_data["password_confirmation"]

        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        # patronymic = self.cleaned_data["patronymic"]

        User = get_user_model()
        user = User.objects.create_user(
            username=email, email=email, password=password
        )
        user.first_name = first_name
        user.last_name = last_name
        # if patronymic:
        #     user.patronymic = patronymic
        user.save()

        return user
