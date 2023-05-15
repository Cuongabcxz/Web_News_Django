from django.shortcuts import render, get_object_or_404

from .models import Comment
from .forms import CommentForm


# Create your views here.
def comment(request):
    comment_list = Comment.objects.all().filter()
    context = {
        'comment_list': comment_list,
    }
    return render(request, 'users/comment/comment.html', context)


def comment_create(request):
    template = 'users/comment/add_comment.html'
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return render(request, 'users/comment/comment.html', {})
    else:
        comment_form = CommentForm()
    context = {
        'comment_form': comment_form,
    }
    return render(request, template, context=context)


def comment_update(request, comment_id=None):
    comment = Comment.objects.get(id=comment_id)
    comment_form = CommentForm(instance=comment)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return render(request, 'users/comment/update_comment.html')

    context = {
        'comment_form': comment_form,
        'comment': comment,
    }
    return render(request, 'users/comment/update_comment.html', context)


def comment_delete(request, comment_id=None):
    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        comment.delete()
        return render(request, 'users/comment/comment.html')

    context = {
        'comment': comment,
    }
    return render(request, 'users/comment/delete_comment.html', context)
