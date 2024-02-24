from django.urls import path

from articles import views


app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:article_id>/', views.article, name='article'),
    path('articles_by_tag/<slug:slug>/', views.articles_by_tag, name='articles_by_tag'),
    path('articles_by_category/<slug:slug>/', views.articles_by_category, name='articles_by_category')
]
