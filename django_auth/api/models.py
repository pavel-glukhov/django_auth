from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    STANDARD_USER = 'user'
    MODERATOR_USER = 'moderator'
    ADMIN_USER = 'admin'

    UserRole = (
        (STANDARD_USER, 'Пользователь'),
        (MODERATOR_USER, 'Модератор'),
        (ADMIN_USER, 'Администратор')
    )
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    role = models.CharField(max_length=20, choices=UserRole, default=STANDARD_USER)
    confirmation_code = models.CharField(max_length=20, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
