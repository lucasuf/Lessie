from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parse_log_theme', views.parse_log_theme, name='parse_log_theme')
]
