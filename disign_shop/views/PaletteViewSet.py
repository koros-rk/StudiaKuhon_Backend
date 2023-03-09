from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from ..models import Palette
from ..serializers import PaletteSerializer


class PaletteViewSet(viewsets.ModelViewSet):
    serializer_class = PaletteSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Palette.objects.all()
        return queryset
