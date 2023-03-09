from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from ..models import Handle
from ..serializers import HandleSerializer


class HandleViewSet(viewsets.ModelViewSet):
    serializer_class = HandleSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Handle.objects.all()
        return queryset
