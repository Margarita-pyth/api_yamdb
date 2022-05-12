from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''Пользовательские роли'''
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]

    username = models.TextField('Имя пользователя', max_length=100,
                                unique=True)
    email = models.EmailField('Почта', unique=True)
    role = models.CharField('Роль пользователя', max_length=100,
                            choices=ROLE, default=USER)
    bio = models.TextField(verbose_name='О себе', null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def is_user(self):
        '''Роли'''
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN
