from rest_framework import serializers
from ..models import Handle


class HandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handle
        fields = ('title',)
