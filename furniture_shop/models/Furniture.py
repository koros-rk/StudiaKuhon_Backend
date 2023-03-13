from django.db import models
from Category import Category
from FurniturePhoto import FurniturePhoto
from FurnitureColor import FurnitureColor


class Furniture(models.Model):
    # main part
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    main_photo = models.URLField(max_length=500)
    thumbnail_photo = models.URLField(max_length=500)

    # partition part
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gallery = models.ManyToManyField(FurniturePhoto)
    colors = models.ManyToManyField(FurnitureColor, through='Availability')

    # utility part
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Availability(models.Model):
    furniture = models.ForeignKey(Furniture)
    color = models.ForeignKey(FurnitureColor)
    availability = models.BooleanField()
