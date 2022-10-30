from django.db import models


class Social(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    image = models.ImageField()

    def __str__(self) -> str:
        return self.name
