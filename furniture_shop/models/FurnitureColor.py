from django.db import models


class FurnitureColor(models.Model):
    title = models.CharField(max_length=250)
    hash = models.CharField(max_length=100)

    def __str__(self):
        return self.title
