from django.db.models import Q
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from ..models import Product
from ..serializers import ProductSerializer
from ..pagination import SetPaginationProducts
from ..Filters import ProductFilter


def detail_route(url_path):
    pass


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
        product_obj = Product.objects.filter(Q(styles__title__contains=instance.main_style.title)).exclude(pk=instance.pk).order_by('?')[:6]
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

        product_obj = Product.objects.filter(Q(styles__title__contains=product.main_style.title)).exclude(pk=product.pk).order_by('?')[:6]
        related = []
        for k in product_obj:
            ser = self.get_serializer(k)
            related.append(ser.data)
        related_data = serializer.data
        related_data["related"] = related

        return Response(related_data)
