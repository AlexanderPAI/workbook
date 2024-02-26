from django.urls import path

from articles import views


app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:article_id>/', views.article, name='article'),
    path('articles_by_tag/<slug:slug>/', views.articles_by_tag, name='articles_by_tag'),
    path('articles_by_category/<slug:slug>/', views.articles_by_category, name='articles_by_category'),
    path('articles/create/', views.article_create, name='article_create'),
    path('articles/<int:article_id>/edit/', views.article_edit, name='article_edit'),
    path('tags/', views.tags, name='tags'),
    path('tags/<slug:slug>/edit/', views.tag_edit, name='tag_edit'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<slug:slug>/edit/', views. category_edit, name='category_edit'),
]
