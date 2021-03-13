"""Defines URL patterns for blog."""

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # About page
    path('about/', views.about, name='about'),
    # Individual Post Page
    path('posts/<int:post_id>/', views.post, name='post')
]
