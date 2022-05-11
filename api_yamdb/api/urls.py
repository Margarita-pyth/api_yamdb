from django.urls import path
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import get_jwt_token, register, UserViewSet
from api.views import CommentViewSet, ReviewViewSet


router = DefaultRouter()

router.register(r"users", UserViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
