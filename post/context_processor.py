from .models import Topic, News


def topic_links(request):
    topic_list = Topic.objects.all().filter(is_star=True)
    return dict(topic_list=topic_list)


