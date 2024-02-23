from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


COLORS = {
    'white': '#FFFFFF',
    'black': '#000000',
}


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
        'Category',
        on_delete=models.CASCADE,
        related_name='articles',
    )
    tags = models.ManyToManyField(
        'Tag',
        through='TagArticle',
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

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория',
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

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
    text_color = models.CharField(
        max_length=200,
        verbose_name='Цвет текста',
        choices=COLORS,
        default='white',
        blank=True,
        null=True,
    )
    background_color = models.CharField(
        max_length=200,
        verbose_name='Цвет фона',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class TagArticle(models.Model):
    """Вспомогательная модель M2M Тег-Статья."""
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag} {self.article}'
