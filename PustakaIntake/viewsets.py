from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListRetrieveUpdateModelMixin(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                                   GenericViewSet):
    pass

