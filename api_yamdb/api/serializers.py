from datetime import datetime

from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator
from rest_framework import permissions

from reviews.models import Category, Genre, Title


class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(read_only=True)
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())
                    ], required=True,)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())
                    ],
    )

    class Meta:
        model = User
        fields = ('__all__')


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Выберите другой логин.'
            )
        return value


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser)


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class AdminUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Title

    def validate(self, attrs):
        # user = self.context.get('request').user
        # following = attrs.get('following')
        title = attrs.get('title')
        if title.year > datetime.year:
            raise serializers.ValidationError(
                'Будущее еще не наступило!'
            )
        return attrs
