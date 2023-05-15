from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author_id = kwargs.pop('author_id', None)
        super().__init__(*args, **kwargs)

        # update all field using class form-control
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        news = super().save(commit=False)
        news.author_id = self.author_id
        news.save()

    class Meta:
        model = News
        fields = ['title', 'slug', 'image', 'video', 'short_desc', 'content', 'category_id', 'type_id', 'topic_id',
                  'is_display']
