from django.db import models
from slugify import slugify

from .Category import Category
from .FurniturePhoto import FurniturePhoto
from .FurnitureColor import FurnitureColor


class Furniture(models.Model):
    # main part
    title = models.CharField(max_length=100)

    @property
    def slug(self):
        return slugify(self.title)

    description = models.CharField(max_length=200)
    main_photo = models.URLField(max_length=500)
    thumbnail_photo = models.URLField(max_length=500)
    price = models.IntegerField(default=1)
    width = models.IntegerField(default=1)
    height = models.IntegerField(default=1)
    depth = models.IntegerField(default=1)

    # partition part
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gallery = models.ManyToManyField(FurniturePhoto)
    colors = models.ManyToManyField(FurnitureColor, through='ColorAvailability')

    # utility part
    availability = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ColorAvailability(models.Model):
    furniture = models.ForeignKey(Furniture, on_delete=models.PROTECT)
    color = models.ForeignKey(FurnitureColor, on_delete=models.PROTECT)
    availability = models.BooleanField()
