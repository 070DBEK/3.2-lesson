from django.db import models
from django.utils.text import slugify
import random


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1
            while Tag.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{random.randint(1, 1000)}"
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name