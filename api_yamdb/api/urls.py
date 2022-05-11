from django.urls import path
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import token, register, UserViewSet

from api.views import CategoryViewSet, GenreViewSet, TitleViewSet

router_v1 = DefaultRouter()

router_v1.register(r"users", UserViewSet)
router_v1.register('users', UserViewSet, basename='users')
router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('titles', TitleViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', token, name='login'),
]
