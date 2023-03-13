from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from ..models import FurnitureColor
from ..serializers import FurnitureColorSerializer


class FurnitureColorViewSet(viewsets.ModelViewSet):
    serializer_class = FurnitureColorSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = FurnitureColor.objects.all()
        return queryset
