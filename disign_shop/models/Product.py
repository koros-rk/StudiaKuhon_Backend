from django.db import models
from slugify import slugify

from .Photo import Photo
from .Style import Style
from .Handle import Handle
from .Material import Material
from .Palette import Palette


class Product(models.Model):
    # main part
    title = models.CharField(max_length=100)
    description_shorted = models.CharField(max_length=200)
    description_full = models.TextField()
    main_photo = models.URLField(max_length=500)
    thumbnail_photo = models.URLField(max_length=500)

    @property
    def slug(self):
        return slugify(self.title)

    # partition part
    gallery = models.ManyToManyField(Photo)
    styles = models.ManyToManyField(Style)
    colours = models.ManyToManyField(Palette)
    materials = models.ManyToManyField(Material)
    handle = models.ForeignKey(Handle, on_delete=models.CASCADE)

    main_colour = models.ForeignKey(Palette, on_delete=models.CASCADE, related_name="color", verbose_name="main_color",
                                    null=True)
    main_style = models.ForeignKey(Style, on_delete=models.CASCADE, related_name="style", verbose_name="main_style",
                                   null=True)
    main_material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="material",
                                      verbose_name="main_material", null=True)

    # utility part
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title
