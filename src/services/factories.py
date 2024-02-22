import factory
# import factory.fuzzy

from django.contrib.auth.models import User

from factory.django import DjangoModelFactory

from articles.models import Article, Category, Tag, TagArticle


class UserFactory(DjangoModelFactory):
    """Генератор пользователей."""
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda n: '{0}@test.com'.format(n.username).lower())


class CategoryFactory(DjangoModelFactory):
    """Генератор категорий."""
    class Meta:
        model = Category

    name = factory.Faker(
        'sentence',
        nb_words=1,
        variable_nb_words=True
    )
    slug = factory.LazyAttribute(lambda n: '{0}'.format(n.name).lower())


class TagFactory(DjangoModelFactory):
    """Генератор тегов."""
    class Meta:
        model = Tag

    name = factory.Faker(
        'sentence',
        nb_words=1,
        variable_nb_words=True
    )
    slug = factory.LazyAttribute(lambda n: '{0}'.format(n.name).lower())


class TagArticleFactory(DjangoModelFactory):
    class Meta:
        model = TagArticle

    tag = factory.Iterator(Tag.objects.all())
    article = factory.Iterator(Article.objects.all())


class ArticleFactory(DjangoModelFactory):
    """Генератор статей."""
    class Meta:
        model = Article
    author = factory.Iterator(User.objects.all())
    title = factory.Faker(
        'sentence',
        nb_words=4,
        variable_nb_words=True
    )
    text = factory.Faker(
        'sentence',
        nb_words=200,
        variable_nb_words=True
    )
    category = factory.Iterator(Category.objects.all())
    created = factory.Faker(
        'date_time',
    )
    updated = factory.Faker(
        'date_time'
    )


class ArticleWithTags(ArticleFactory):
    tags1 = factory.RelatedFactory(
        TagArticleFactory,
        factory_related_name='article',
        tag__name=factory.Iterator(Tag.objects.all())
    )
    tags2 = factory.RelatedFactory(
        TagArticleFactory,
        factory_related_name='article',
        tag__name=factory.Iterator(Tag.objects.all())
    )
