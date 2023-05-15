from django.urls import path
from . import views

urlpatterns = [
    path('<slug:type_slug>/details/<slug:news_slug>', views.news_detail, name='news_detail'),
    path('search/', views.search, name='search'),
    path('category/<slug:category_slug>', views.news_by_category, name='news_by_category'),
    path('category/<slug:category_slug>/type/<slug:type_slug>', views.news_by_type, name='news_by_type'),
    path('topic/', views.topic, name='topic'),
    path('topic/<slug:topic_slug>', views.topic_detail, name='topic_detail'),
    path('video/', views.video, name='video'),
    path('new/', views.new, name='new'),
    # dashboard
    path('news/<int:id>', views.news, name='news'),
    path('news/news-create/', views.news_create, name='news-create'),
    path('news/news-update/<slug:news_slug>/', views.news_update, name='news-update'),
    path('news/delete/<slug:news_slug>', views.news_delete, name='news-delete')
]
