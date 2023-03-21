from django_filters import rest_framework as filters
from ..models import Product


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    styles = CharFilterInFilter(field_name="styles__title", lookup_expr="in")
    materials = CharFilterInFilter(field_name="materials__title", lookup_expr="in")
    colors = CharFilterInFilter(field_name="colors__title", lookup_expr="in")
    handle = CharFilterInFilter(field_name="handle__title", lookup_expr="in")

    class Meta:
        model = Product
        fields = ['styles', 'materials', 'colors', 'handle']
