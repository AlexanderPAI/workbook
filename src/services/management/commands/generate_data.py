from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

from articles.models import Article, Category, Tag, TagArticle
from services.factories import ArticleFactory, ArticleWithTags, CategoryFactory, TagFactory, TagArticleFactory, UserFactory
NUM_USERS = 3
NUM_ARTICLES = 100
NUM_CATEGORIES = 5
NUM_TAGS = 10


class Command(BaseCommand):
    """Команда для генерации данных."""
    @transaction.atomic
    def handle(self, *args, **options):
        models = [Article, Category, Tag, TagArticle, User]
        for m in models:
            m.objects.all().delete()

        for _ in range(NUM_USERS):
            user = UserFactory()
            print(user.username)

        for _ in range(NUM_CATEGORIES):
            category = CategoryFactory()
            print(category.name)

        for _ in range(NUM_TAGS):
            tag = TagFactory()
            print(tag.name)

        for _ in range(NUM_ARTICLES):
            article = ArticleFactory()
            print(article.title[:15])

        for _ in range(NUM_ARTICLES):
            article_with_tags = ArticleWithTags()
            print(article_with_tags.title[:15])
