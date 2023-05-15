from django.contrib import admin
from .models import Comment


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'news_id', 'content', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('user_id', 'news_id', 'content')


admin.site.register(Comment, CommentAdmin)
