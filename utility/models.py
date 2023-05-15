from django.db import models
from django.urls import reverse


# Create your models here.
class Utility(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='')

    def get_url(self):
        return reverse('utility', args=[self.slug])

    class Meta:
        verbose_name = 'utility'
        verbose_name_plural = 'utilities'

    def __str__(self):
        return self.name
