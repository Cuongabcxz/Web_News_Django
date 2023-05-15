from django.contrib import admin
from django import forms
from .models import News, Topic
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.
class NewsForm(forms.Form):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    froms = NewsForm
    prepopulated_fields = {'slug': ('title',)}  # Gợi ý trường slug theo title
    list_display = ('title', 'category_id', 'type_id', 'author_id', 'created_date', 'is_display')


class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Gợi ý trường slug theo title
    list_display = ('name', 'slug')


admin.site.register(News, NewsAdmin)
admin.site.register(Topic, TopicAdmin)
