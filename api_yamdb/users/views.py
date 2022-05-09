from .models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from api_yamdb.settings import DEFAULT_FROM_EMAIL
from rest_framework.permissions import AllowAny
from api.serializers import UserSerializer, TokenSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import AccessToken
from api.serializers import IsAdmin


class APIRegistrUser(APIView):
    '''Регистрация пользователя'''
    permission_classes = (AllowAny, )


def register(self, request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        create_code_and_email(
            serializer.data['username'])
    return Response(serializer.data, status=status.HTTP_200_OK)


def create_code_and_email(username):
    '''Отправляем код на почту'''
    user = get_object_or_404(User, username=username)
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        confirmation_code='Регистрация',
        message=f'Ваш код {confirmation_code}',
        from_email=DEFAULT_FROM_EMAIL,
        email_list=['user.email'])


class APIToken(APIView):
    permission_classes = (AllowAny, )


def get_jwt_token(request):
    '''Получение токена'''
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid()
    user = get_object_or_404(
        User,
        username=serializer.validated_data["username"]
    )
    if default_token_generator.check_token(
        user, serializer.validated_data["confirmation_code"]
    ):
        token = AccessToken.for_user(user)
        return Response({"token": str(token)}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    search_fields = ['username', ]

    @action(
        methods=["get", "patch", ],
        detail=False,
        url_path="me",
        permission_classes=[permissions.IsAuthenticated],
        serializer_class=UserSerializer,
    )
    def profile_user(self, request):
        '''Заполнение личных данных в профайле'''
        user = request.user
        if request.method == "GET":
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == "PATCH":
            serializer = self.get_serializer(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
