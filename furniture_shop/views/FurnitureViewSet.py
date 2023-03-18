from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response

from ..models import Furniture
from ..serializers import FurnitureSerializer
from ..pagination import SetPaginationFurniture


class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    pagination_class = SetPaginationFurniture

    def get_queryset(self):
        queryset = Furniture.objects.all().filter(show=True)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        product_obj = Furniture.objects.filter(category=instance.category.id).exclude(pk=instance.pk).order_by('?')[:6]
        related = []
        for k in product_obj:
            ser = self.get_serializer(k)
            related.append(ser.data)
        related_data = serializer.data
        related_data["related"] = related
        return Response(related_data)

    @action(detail=False, methods=['GET'], url_path='slug/(?P<slug>[^/.]+)')
    def get_by_slug(self, request, slug=None):
        queryset = self.get_queryset()
        product = [i for i in queryset if i.slug == slug][0]
        serializer = self.get_serializer(product)

        product_obj = Furniture.objects.filter(category=product.category.id).exclude(pk=product.pk).order_by('?')[:6]
        related = []
        for k in product_obj:
            ser = self.get_serializer(k)
            related.append(ser.data)
        related_data = serializer.data
        related_data["related"] = related

        return Response(related_data)
