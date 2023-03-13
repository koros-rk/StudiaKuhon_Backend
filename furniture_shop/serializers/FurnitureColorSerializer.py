from rest_framework import serializers
from ..models import FurnitureColor


class FurnitureColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureColor
        fields = ('title', 'hash')
