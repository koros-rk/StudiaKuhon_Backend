from rest_framework import serializers

from ..models import *
from .FurniturePhotoSerializer import FurniturePhotoSerializer
from .FurnitureColorSerializer import FurnitureColorSerializer
from .CategorySerializer import CategorySerializer


class FurnitureSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    gallery = FurniturePhotoSerializer(many=True)
    colors = FurnitureColorSerializer(many=True)

    class Meta:
        model = Furniture
        fields = ('id', 'title', 'description', 'main_photo', 'thumbnail_photo', 'category', 'gallery', 'colors', 'time_created', 'time_updated', 'show')

    def create(self, validated_data):

        new_product = Furniture.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            main_photo=validated_data['main_photo'],
            thumbnail_photo=validated_data['thumbnail_photo'],
            category=Category.objects.get(title=validated_data['category']['title']),
            show=True
        )

        for photo in validated_data['gallery']:
            photo_obj = FurniturePhoto.objects.create(url=photo['url'])
            new_product.gallery.add(photo_obj)

        for color in validated_data['colors']:
            color_obj = FurnitureColor.objects.get_or_create(title=color['title'], hash=color['hash'])[0]
            ColorAvailability.objects.create(
                furniture=new_product,
                color=color_obj,
                availability=True
            )

        serializer = FurnitureSerializer(new_product)

        return serializer.data

    def update(self, instance, validated_data):
        updated_gallery_data = validated_data.pop('gallery', [])
        updated_colors_data = validated_data.pop('colors', [])
        updated_category_data = validated_data.pop('category', [])

        instance.gallery.all().delete()
        instance.colors.all().delete()

        new_gallery = []
        for photo_data in updated_gallery_data:
            new_photo = FurniturePhoto.objects.get_or_create(url=photo_data['url'])[0].id
            new_gallery.append(new_photo)

        for color_data in updated_colors_data:
            new_color = FurnitureColor.objects.get_or_create(hash=color_data['hash'], title=color_data['title'])[0]
            ColorAvailability.objects.get_or_create(
                furniture=instance,
                color=new_color,
                availability=True
            )

        instance = super().update(instance, validated_data)

        instance.gallery.set(new_gallery)
        instance.category = Category.objects.get(title=updated_category_data['title'])

        instance.save()

        return instance

