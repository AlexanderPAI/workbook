from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Article(models.Model):
    """Модель статьи."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='Автор',
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    category = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        related_name='articles',
    )
    tags = models.ManyToManyField(
        'Tag',
        through='GenreArticle',
    )
    image = models.ImageField(
        upload_to='articles/',
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
        db_index=True,
    )

    class Meta:
        ordering = ['-created']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title[:15]


class Category(models.Model):
    """Модель категории."""
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    slug = models.SlugField(
        unique=True,
        max_length=200,
        verbose_name='Slug'
    )

class Tag(models.Model):
    """Модель тега."""
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='Slug'
    )


class TagArticle(models.Model):
    """Вспомогательная модель M2M Тег-Статья."""
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag} {self.article}'
