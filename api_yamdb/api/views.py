from rest_framework import filters
# from rest_framework import views
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Category, Genre, Title
from .serializers import (
    CategorySerializer, GenreSerializer, TitleSerializer
)
from .mixins import CreatListDeleteViewSet, NoPutViewSet, PermissionsViewSet
from .permissions import AdminOrReadOnly


class CategoryViewSet(CreatListDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = (AdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    # удалять категорию (и жанр) не по id, а по slug.
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class GenreViewSet(CreatListDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    permission_classes = (AdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(NoPutViewSet, PermissionsViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

    permission_classes = (AdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'year', 'genre__slug', 'category__slug',)
