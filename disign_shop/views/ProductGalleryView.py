from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Product
from ..serializers import ProductSerializer


class ProductGallery(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        instance = Product.objects.filter().order_by('?')[:5]
        serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data)
