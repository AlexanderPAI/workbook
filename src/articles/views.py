from django.core.paginator import Paginator

from django.shortcuts import render, redirect, get_object_or_404

from articles.decorators import superuser_only
from articles.forms import ArticleForm, CategoryForm, TagForm
from articles.models import Article, Category, Tag


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


@superuser_only
def article_create(request):
    """Представление для создания статьи."""
    tags = Tag.objects.all()
    if request.method == 'POST' or None:
        form = ArticleForm(request.POST, files=request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('articles:index')
        return render(
            request,
            'articles/article_create.html',
            {
                'form': form,
                'is_edit': False,
                'tags': tags,
            }
        )
    form = ArticleForm()
    return render(
        request,
        'articles/article_create.html',
        {
            'form': form,
            'is_edit': False,
            'tags': tags
        }
    )


@superuser_only
def article_edit(request, article_id):
    """Представление для редактирования статьи."""
    article = get_object_or_404(Article, pk=article_id)
    tags = Tag.objects.all()
    form = ArticleForm(
        request.POST or None,
        files=request.FILES or None,
        instance=article
    )
    if request.user.is_superuser:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('articles:article', article_id)
            return render(
                request,
                'articles/article_create.html',
                {
                    'form': form,
                    'is_edit': True,
                    'tags': tags,
                }
            )
        return render(
            request,
            'articles/article_create.html',
            {
                'form': form,
                'is_edit': True,
                'tags': tags,
            }
        )
    return redirect('articles/article_create.html', article_id)


def tags(request):
    """Представление для создания тега."""
    tags = Tag.objects.all()
    if request.method == 'POST' or None:
        form = TagForm(request.POST or None)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.save()
            return redirect('articles:tags')
        return render(
            request,
            'articles/tags.html',
            {
                'form': form,
                'is_edit': False,
                'tags': tags,
            }
        )
    form = TagForm()
    return render(
        request,
        'articles/tags.html',
        {
            'form': form,
            'is_edit': False,
            'tags': tags
        }
    )


def tag_edit(request, slug):
    """Представление для редактирования тега."""
    tag = get_object_or_404(Tag, slug=slug)
    tags = Tag.objects.all()
    form = TagForm(
        request.POST or None,
        instance=tag,
    )
    if request.user.is_superuser:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('articles:tags')
            return render(
                request,
                'articles/tags.html',
                {
                    'form': form,
                    'is_edit': True,
                    'tags': tags,
                }
            )
        return render(
            request,
            'articles/tags.html',
            {
                'form': form,
                'is_edit': True,
                'tags': tags,
            }
        )
    return redirect('articles/tags.html', slug)


def category_create(request):
    """Представление для создания раздела."""
    categories = Category.objects.all()
    if request.method == 'POST' or None:
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('articles:articles_by_category', slug=category.slug)
        return render(
            request,
            'articles/category_create.html',
            {
                'form': form,
                'is_edit': False,
                'categories': categories,
            }
        )
    form = CategoryForm()
    return render(
        request,
        'articles/category_create.html',
        {
            'form': form,
            'is_edit': False,
            'categories': categories,
        }
    )


def category_edit(request, slug):
    """Представление для редактирования тега."""
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    form = CategoryForm(
        request.POST or None,
        instance=category,
    )
    if request.user.is_superuser:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('articles:articles_by_category')
            return render(
                request,
                'articles/category_create.html',
                {
                    'form': form,
                    'is_edit': True,
                    'categories': categories,
                }
            )
        return render(
            request,
            'articles/category_create.html',
            {
                'form': form,
                'is_edit': True,
                'categories': categories,
            }
        )
    return redirect('articles/category_create.html', slug)
