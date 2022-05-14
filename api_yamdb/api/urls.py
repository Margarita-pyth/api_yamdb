from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import token, register, UserViewSet
from api.views import (CategoryViewSet,
                       GenreViewSet,
                       TitleViewSet,
                       CommentViewSet,
                       ReviewViewSet)

from api.routers import CustomRouter


router = CustomRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', token, name='login'),
]
