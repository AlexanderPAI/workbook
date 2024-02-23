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
    articles = Article.objects.all()
    page_obj = paginator(request, articles)
    context = {
        'page_obj': page_obj
    }
    return render(
        request,
        'index.html',
        context,
    )


def article(request, article_id):
    """Представление статьи."""
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article
    }
    return render(request, 'articles/article.html', context)
