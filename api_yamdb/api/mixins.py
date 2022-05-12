from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PermissionsViewSet(viewsets.GenericViewSet):
    def get_permissions(self):
        if self.action == 'retrieve':
            return (IsAuthenticatedOrReadOnly(),)
        return super().get_permissions()


class CreatListDeleteViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass
