from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.pop('user_id', None)
        self.news_id = kwargs.pop('news_id', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.user_id = self.user_id
        comment.news_id = self.news_id
        comment.save()

    class Meta:
        model = Comment
        fields = ['content', 'image', 'video', 'file', 'parent']

