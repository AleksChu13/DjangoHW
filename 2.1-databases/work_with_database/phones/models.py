from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)