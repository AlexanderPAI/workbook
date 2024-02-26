from django.contrib import admin

from articles.models import Article, Category, Tag, TagArticle


class TagArticleInLine(admin.TabularInline):
    model = TagArticle
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'title',
        'category',
        'created',
        'updated',
    )
    inlines = (TagArticleInLine,)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
