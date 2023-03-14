from rest_framework import serializers
from rest_framework.utils import model_meta

from ..models import *
from .StyleSerializer import StyleSerializer
from .MaterialSerializer import MaterialSerializer
from .PhotoSerializer import PhotoSerializer
from .HandleSerializer import HandleSerializer
from .PaletteSerializer import PaletteSerializer


class ProductSerializer(serializers.ModelSerializer):
    obj_dict = {
        'handle': Handle.objects,
        'main_colour': Palette.objects,
        'main_style': Style.objects,
        'main_material': Material.objects,
        'gallery': Photo.objects,
        'colours': Palette.objects,
        'styles': Style.objects,
        'materials': Material.objects,
    }

    gallery = PhotoSerializer(many=True)
    styles = StyleSerializer(many=True)
    colours = PaletteSerializer(many=True)
    materials = MaterialSerializer(many=True)
    handle = HandleSerializer()
    main_colour = PaletteSerializer()
    main_style = StyleSerializer()
    main_material = MaterialSerializer()

    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'description_shorted', 'description_full', 'main_photo', 'thumbnail_photo', 'gallery',
                  'styles', 'colours', 'materials', 'handle', 'main_colour', 'main_style', 'main_material',)

    def create(self, validated_data):

        new_product = Product.objects.create(
            title=validated_data['title'],
            description_shorted=validated_data['description_shorted'],
            description_full=validated_data['description_full'],
            main_photo=validated_data['main_photo'],
            thumbnail_photo=validated_data['thumbnail_photo'],
            handle=Handle.objects.get(title=validated_data['handle']['title']),
            main_style=Style.objects.get(title=validated_data['main_style']['title']),
            main_material=Material.objects.get(title=validated_data['main_material']['title']),
            main_colour=Palette.objects.get(title=validated_data['main_colour']['title']),
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

        for color in validated_data['colours']:
            color_obj = Palette.objects.get(title=color['title'])
            new_product.colours.add(color_obj)

        serializer = ProductSerializer(new_product)

        return serializer.data

    def update(self, instance, validated_data):
        info = model_meta.get_field_info(instance)

        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            elif attr in info.relations:
                for k, v in value.items():
                    setattr(instance, attr, self.obj_dict[attr].get(title=v))
            else:
                setattr(instance, attr, value)

        instance.save()

        for attr, value in m2m_fields:
            for i in value:
                for k, v in i.items():
                    match attr:
                        case 'gallery':
                            instance.gallery.add(Photo.objects.get_or_create(url=v)[0].id)
                        case 'styles':
                            instance.styles.add(Style.objects.get(title=v))
                        case 'colors':
                            instance.colours.add(Palette.objects.get(title=v))
                        case 'materials':
                            instance.materials.add(Material.objects.get(title=v))

        return instance
