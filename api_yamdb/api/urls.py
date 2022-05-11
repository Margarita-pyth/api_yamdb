from django.urls import path
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import token, register, UserViewSet

router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', token, name='login'),
]
