from django.db import models


class FurniturePhoto(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url
