from django_filters import rest_framework as filters
from ..models import Furniture


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class FurnitureFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name="category__title", lookup_expr="in")

    class Meta:
        model = Furniture
        fields = ['category']
