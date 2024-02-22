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
