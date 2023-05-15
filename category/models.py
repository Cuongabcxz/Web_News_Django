from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('news_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'types'

    def get_url(self):
        return reverse('news_by_type', args=[self.category_id.slug, self.slug])

    def __str__(self):
        return self.name
