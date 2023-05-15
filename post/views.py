from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from accounts.models import Account
from post.models import News, Topic
from category.models import Category, Type

from review.forms import CommentForm
from post.forms import NewsForm
# Create your views here.


def news_by_category(request, category_slug=None):
    category_name = None
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        category_name = Category.objects.get(name=categories.name)
        news_list = News.objects.all().filter(category_id=categories)
    else:
        news_list = News.objects.all().filter().order_by('id')
    context = {
        'news_list': news_list,
        'category_name': category_name
    }
    return render(request, 'category/news_by_category.html', context)


def news_by_type(request, category_slug, type_slug=None):
    category_name = None
    type_name = None
    news_list = None
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        category_name = Category.objects.get(name=categories.name)
        if type_slug is not None:
            types = get_object_or_404(Type, slug=type_slug)
            type_name = Type.objects.get(name=types.name)
            news_list = News.objects.all().filter(category_id=categories, type_id=types)
    else:
        news_list = News.objects.all().filter().order_by('id')

    context = {
        'news_list': news_list,
        'category_name': category_name,
        'type_name': type_name
    }
    return render(request, 'category/type/news_by_type.html', context)


def topic(request):
    # topic_links = Topic.objects.all()
    # context = {
    #     'topic_links': topic_links
    # }
    return render(request, 'post/topic/topicPage.html')


def topic_detail(request, topic_slug=None):
    topics = None
    if topic_slug is not None:
        topics = get_object_or_404(Topic, slug=topic_slug)
        news_list = News.objects.all().filter(topic_id=topics)
    else:
        news_list = News.objects.all().filter().order_by('id')
    context = {
        'news_list': news_list,
        'topics': topics
    }
    return render(request, 'post/topic/topic_details.html', context)


def video(request):
    video_links = News.objects.all().exclude(video__isnull=True).exclude(video__exact='')
    context = {
        'video_links': video_links,
    }
    return render(request, 'post/video/videoPage.html', context=context)


def new(request):
    news_list = News.objects.all()
    context = {
        'news_list': news_list
    }
    return render(request, 'post/new/newPage.html', context)


def search(request):
    news_list = None
    q = None
    news_count = None
    if 'q' in request.GET:
        q = request.GET.get('q')
        news_list = News.objects.order_by('-created_date').filter(
            Q(category_id__news__title__icontains=q) | Q(short_desc__icontains=q))
        news_count = news_list.count()
    context = {
        'news_list': news_list,
        'q': q,
        'news_count': news_count
    }
    return render(request, 'includes/result_search.html', context=context)


def news_detail(request, type_slug, news_slug=None):
    type_name = None
    single_news = None
    if type_slug is not None:
        types = get_object_or_404(Type, slug=type_slug)
        type_name = Type.objects.get(name=types.name)
        single_news = get_object_or_404(News, type_id=types, slug=news_slug)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES,
                                   user_id=request.user, news_id=single_news)
        if comment_form.is_valid():
            if not request.user.is_authenticated:
                return render(request, 'accounts/login.html', {})
            comment_form.save()
    else:
        comment_form = CommentForm()
    context = {
        'type_name': type_name,
        'single_news': single_news,
        'comment_form': comment_form,
    }
    return render(request, 'post/news_details.html', context=context)


def news(request, id=None):
    author = Account.objects.get(id=id)
    news_list = News.objects.all().filter(author_id=author.id)
    context = {
        'news_list': news_list,
        'author': author
    }
    return render(request, 'users/post/news.html', context)


def news_create(request):
    # dictionary for initial data with
    # field names as keys
    # add the dictionary during initialization
    if request.method == 'POST':
        news_form = NewsForm(request.POST, request.FILES, author_id=request.user)
        if news_form.is_valid():
            print('Lưu bài viết')
            news_form.save()
            return render(request, 'users/post/news.html', {})
    else:
        print('Thêm bài viết')
        news_form = NewsForm(author_id=request.user)

    context = {
        'news_form': news_form,
    }
    return render(request, "users/post/add_news.html", context)


def news_update(request, news_slug=None):
    single_news = News.objects.get(slug=news_slug)
    news_form = NewsForm(instance=single_news, author_id=request.user)

    if request.method == 'POST':
        news_form = NewsForm(request.POST, request.FILES, author_id=request.user,instance=single_news)
        if news_form.is_valid():
            news_form.save()
            return render(request, 'users/post/news.html')

    context = {
        'news_form': news_form,
        'single_news': single_news,
    }
    return render(request, 'users/post/update_news.html', context)


def news_delete(request, news_slug=None):
    single_news = News.objects.get(slug=news_slug)

    if request.method == 'POST':
        single_news.delete()
        return render(request, 'users/post/news.html')

    context = {
        'single_news': single_news,
    }
    return render(request, 'users/post/delete_news.html', context)