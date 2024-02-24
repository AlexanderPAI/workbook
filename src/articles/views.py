from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404

from articles.models import Article, Category, Tag, User

PAGE_SIZE = 10

def paginator(request, articles):
    paginator = Paginator(articles, PAGE_SIZE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    """Представление главной страницы."""
    tags = Tag.objects.all()
    articles = Article.objects.all()
    page_obj = paginator(request, articles)
    context = {
        'page_obj': page_obj,
        'tags': tags,
    }
    return render(
        request,
        'index.html',
        context,
    )


def article(request, article_id):
    """Представление одной статьи."""
    tags = Tag.objects.all()
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
        'tags': tags,
    }
    return render(request, 'articles/article.html', context)


def articles_by_tag(request, slug):
    """Представление фильтра по тегу."""
    tags = Tag.objects.all()
    tag = get_object_or_404(Tag, slug=slug)
    articles = tag.articles.all()
    page_obj = paginator(request, articles)
    context = {
        'page_obj': page_obj,
        'tag': tag,
        'tags': tags,
    }
    return render(request, 'articles/articles_by_tag.html', context)


def articles_by_category(request, slug):
    """Представление фильтра по разделу."""
    tags = Tag.objects.all()
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.all()
    page_obj = paginator(request, articles)
    context = {
        'page_obj': page_obj,
        'category': category,
        'tags': tags,
    }
    return render(request, 'articles/articles_by_category.html', context)