from django.db import models
from django.conf import settings


class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True,blank=True)
    url = models.TextField(max_length=200)

    def __str__(self):
        return self.title


