from rest_framework.serializers import Serializer, CharField, EmailField, ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]


class UserRegisterSerializer(Serializer):
    email = EmailField(required=True, write_only=True)
    username = CharField(required=True, write_only=True)


class UserConfirmationSerializer(Serializer):
    email = EmailField(required=True, write_only=True)
    confirmation_code = CharField(required=True, write_only=True)
