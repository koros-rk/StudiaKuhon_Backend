from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from ..models import Product
from ..serializers import ProductSerializer
from ..pagination import SetPaginationProducts
from ..Filters import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().filter(show=True)
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = SetPaginationProducts

    def get_queryset(self):
        return self.queryset.distinct()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        product_obj = Product.objects.filter(~Q(id=instance.id), main_material=instance.main_material.id)
        related = []
        for k in product_obj:
            ser = self.get_serializer(k)
            related.append(ser.data)
        related_data = serializer.data
        related_data["related"] = related
        return Response(related_data)
