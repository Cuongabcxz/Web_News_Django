from django.urls import path
from . import views

urlpatterns = [
# dashboard
    path('', views.comment, name='comment'),
]
