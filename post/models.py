from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from category.models import Category, Type
from accounts.models import Account
from ckeditor.fields import RichTextField


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='static/Images', null=True, blank=True)
    is_star = models.BooleanField(default=False, null=True, blank=True)

    def get_url(self):
        return reverse('topic_detail', args=[self.slug])

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'topics'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='photos/post/news')
    video = models.FileField(upload_to='photos/post/news', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    short_desc = models.TextField()
    content = RichTextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)  # Khi xóa category thì News bị xóa
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_display = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'news'

    def get_url(self):
        return reverse('news_detail', args=[self.type_id.slug, self.slug])

    def duration_day(self):
        date_now = timezone.now()
        duration = date_now - self.created_date
        return duration.days

    @property
    def duration(self):
        minute = 60
        hour = minute * 60
        day = hour * 24
        date_now = timezone.now()
        duration = date_now - self.created_date
        duration_in_s = duration.total_seconds()
        if minute <= duration_in_s < hour:
            date_till_stripped = " ".join([str(round(divmod(duration_in_s, minute)[0])), 'phút trước'])
        elif hour <= duration_in_s < day:
            date_till_stripped = " ".join([str(round(divmod(duration_in_s, hour)[0])), 'giờ  trước'])
        else:
            date_till_stripped = " ".join([str(duration.days), 'ngày trước'])
        return date_till_stripped

    def __str__(self):
        return self.title
