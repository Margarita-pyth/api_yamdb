from django.urls import path
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import get_jwt_token, register, UserViewSet

from api.views import CategoryViewSet, GenreViewSet, TitleViewSet

router = DefaultRouter()

router.register(r"users", UserViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token'),
    path('v1/', include(router.urls)),
]
