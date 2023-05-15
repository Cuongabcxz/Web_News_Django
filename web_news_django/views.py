from django.shortcuts import render

from post.models import News


def home(request):
    news_list = News.objects.all().filter()
    context = {
        'news_list': news_list,
    }
    return render(request, 'index.html', context=context)
