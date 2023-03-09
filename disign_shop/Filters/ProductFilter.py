from django_filters import rest_framework as filters
from ..models import Product


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    styles = CharFilterInFilter(field_name="styles__title", lookup_expr="in")
    materials = CharFilterInFilter(field_name="materials__title", lookup_expr="in")
    colours = CharFilterInFilter(field_name="colours__title", lookup_expr="in")

    class Meta:
        model = Product
        fields = ['styles', 'materials', 'colours']