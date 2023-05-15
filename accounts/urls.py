from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('register/', views.register, name='register'),
    path('dashboards/<id>/', views.dashboard_users, name='dashboard_users'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]
