import jwt
from apps.base.v1.serializers import UserSerializer
from django import forms
from django.contrib.auth import get_user_model
from service_objects.services import Service


class GetUserCookieHttponly(Service):
    """Сервис для получения id пользователя из cookie request"""

    token = forms.CharField()

    def process(self):
        token = self.cleaned_data["token"]
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        user_id = decoded_token["user_id"]
        User = get_user_model()
        user = User.objects.get(id=user_id)

        return UserSerializer(user)
