from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from ..models import FurniturePhoto
from ..serializers import FurniturePhotoSerializer


class FurniturePhotoViewSet(viewsets.ModelViewSet):
    serializer_class = FurniturePhotoSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = FurniturePhoto.objects.all()
        return queryset
