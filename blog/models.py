from django.db import models


class Social(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    image = models.URLField()

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
