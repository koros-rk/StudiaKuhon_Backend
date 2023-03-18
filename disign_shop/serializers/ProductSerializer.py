from rest_framework import serializers

from ..models import *
from .StyleSerializer import StyleSerializer
from .MaterialSerializer import MaterialSerializer
from .PhotoSerializer import PhotoSerializer
from .HandleSerializer import HandleSerializer
from .PaletteSerializer import PaletteSerializer


class ProductSerializer(serializers.ModelSerializer):
    obj_dict = {
        'handle': Handle.objects,
        'main_style': Style.objects,
        'gallery': Photo.objects,
        'colors': Palette.objects,
        'styles': Style.objects,
        'materials': Material.objects,
    }

    gallery = PhotoSerializer(many=True)
    styles = StyleSerializer(many=True)
    colors = PaletteSerializer(many=True)
    materials = MaterialSerializer(many=True)
    handle = HandleSerializer()
    main_style = StyleSerializer()

    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'description_shorted', 'description_full', 'main_photo', 'thumbnail_photo', 'gallery',
                  'styles', 'colors', 'materials', 'handle', 'main_style',)

    def create(self, validated_data):

        new_product = Product.objects.create(
            title=validated_data['title'],
            description_shorted=validated_data['description_shorted'],
            description_full=validated_data['description_full'],
            main_photo=validated_data['main_photo'],
            thumbnail_photo=validated_data['thumbnail_photo'],
            handle=Handle.objects.get(title=validated_data['handle']['title']),
            main_style=Style.objects.get(title=validated_data['main_style']['title']),
            show=True
        )

        for photo in validated_data['gallery']:
            photo_obj = Photo.objects.create(url=photo['url'])
            new_product.gallery.add(photo_obj)

        for style in validated_data['styles']:
            style_obj = Style.objects.get(title=style['title'])
            new_product.styles.add(style_obj)

        for material in validated_data['materials']:
            material_obj = Material.objects.get(title=material['title'])
            new_product.materials.add(material_obj)

        for color in validated_data['colors']:
            color_obj = Palette.objects.get(title=color['title'])
            new_product.colours.add(color_obj)

        serializer = ProductSerializer(new_product)

        return serializer.data

    def update(self, instance, validated_data):
        updated_gallery_data = validated_data.pop('gallery', [])
        updated_style_data = validated_data.pop('styles', [])
        updated_colors_data = validated_data.pop('colors', [])
        updated_materials_data = validated_data.pop('materials', [])
        updated_handle_data = validated_data.pop('handle', [])
        updated_main_style_data = validated_data.pop('main_style', [])

        instance.gallery.all().delete()
        instance.styles.clear()
        instance.colors.clear()
        instance.materials.clear()

        instance = super().update(instance, validated_data)

        new_gallery = []
        for photo_data in updated_gallery_data:
            new_photo = Photo.objects.get_or_create(url=photo_data['url'])[0].id
            new_gallery.append(new_photo)

        new_styles = []
        for style_data in updated_style_data:
            new_photo = Style.objects.get(title=style_data['title']).id
            new_styles.append(new_photo)

        new_colors = []
        for color_data in updated_colors_data:
            new_color = Palette.objects.get(title=color_data['title']).id
            new_colors.append(new_color)

        new_materials = []
        for material_data in updated_materials_data:
            new_material = Material.objects.get(title=material_data['title']).id
            new_materials.append(new_material)

        instance.gallery.set(new_gallery)
        instance.styles.set(new_styles)
        instance.colors.set(new_colors)
        instance.materials.set(new_materials)
        instance.handle = Handle.objects.get(title=updated_handle_data['title'])
        instance.main_style = Style.objects.get(title=updated_main_style_data['title'])

        instance.save()

        return instance
