from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from django.utils.crypto import get_random_string
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import (
    UserConfirmationSerializer,
    UserRegisterSerializer,
    UserSerializer
)
from rest_framework_simplejwt.tokens import AccessToken
from django.db.models import Q


class CreateTokenView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = UserConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        confirmation_code = serializer.validated_data['confirmation_code']

        user = get_object_or_404(User, email=email)

        if user.confirmation_code == confirmation_code:
            access_token = AccessToken.for_user(user=user)
            return Response({"access_token": str(access_token)})
        return Response('Please check your credentials')


class Signup(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        username = serializer.validated_data['username']

        user = User.objects.filter(Q(email=email) | Q(username=username)).exists()

        if not user:
            confirmation_code = get_random_string(length=12)

            User.objects.create_user(
                email=email,
                username=username,
                confirmation_code=confirmation_code
            )
            return Response(
                {'confirmation code': confirmation_code}
            )
        return Response('The user already exist')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

    @action(
        detail=False,
        methods=['get', ],
        permission_classes=[IsAuthenticated, ]
    )
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
