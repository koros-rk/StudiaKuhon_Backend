from rest_framework import serializers
from ..models import FurnitureColor, ColorAvailability


class FurnitureColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = FurnitureColor
        fields = ('title', 'hash',)


class ColorAvailabilitySerializer(serializers.ModelSerializer):
    color = FurnitureColorSerializer()

    class Meta:
        model = ColorAvailability
        fields = ['color', 'availability']
