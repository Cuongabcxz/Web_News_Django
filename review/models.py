from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from accounts.models import Account
from post.models import News


# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='photos/comments', null=True, blank=True)
    video = models.FileField(upload_to='photos/comments', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    file = models.FileField(upload_to='', null=True, blank=True)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'comments'
        ordering = ('created_date',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user_id.username, self.news_id.title)

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

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
