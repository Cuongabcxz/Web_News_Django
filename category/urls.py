from django.urls import path
from . import views

urlpatterns = [
    # dashboard
    path('', views.category, name='category'),
    path('category-create/', views.category_create, name='category-create'),
    path('category-update/<slug:category_slug>/', views.category_update, name='category-update'),
    path('category-delete/<slug:category_slug>/', views.category_delete, name='category-delete')
]