from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Category, Genre, Title, Review
from api.serializers import (CategorySerializer,
                             GenreSerializer,
                             TitleSerializer,
                             ReviewSerializer,
                             CommentSerializer)
from api.permissions import AdminOrReadOnly, IsAdminModeratorOwnerOrReadOnly
from api.mixins import CreatListDeleteViewSet, NoPutViewSet, PermissionsViewSet
# from rest_framework.response import Response
# from rest_framework import status


class CategoryViewSet(CreatListDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = (AdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    # удалять категорию (и жанр) не по id, а по slug.
    # def destroy(self, request, *args, **kwargs):
    #    slug = self.kwargs.get('slug')
    #    id = Category.objects.filter(slug=slug)
    #    instance = get_object_or_404(Category, id=id)
    #    self.perform_destroy(instance)
    #    return Response(status=status.HTTP_204_NO_CONTENT)

    # def perform_destroy(self, instance):
    #    slug = self.kwargs.get('slug')
    #    id = Category.objects.filter(slug=slug)
    #    category = get_object_or_404(Category, id=id)
    #    instance.delete(category)


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


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminModeratorOwnerOrReadOnly]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get("title_id"))

        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAdminModeratorOwnerOrReadOnly]

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get("review_id"))
        return review.comments.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id, title=title_id)
        serializer.save(author=self.request.user, review=review)
