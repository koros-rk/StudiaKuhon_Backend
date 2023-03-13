from rest_framework import serializers
from ..models import FurniturePhoto


class FurniturePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurniturePhoto
        fields = ('url',)
