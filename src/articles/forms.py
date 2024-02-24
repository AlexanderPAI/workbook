from django import forms

from tinymce.widgets import TinyMCE

from articles.models import Article, Category, Tag


class ArticleForm(forms.ModelForm):
    """Форма создания/редактирования поста."""
    class Meta:
        model = Article
        widgets = {'text': TinyMCE(attrs={'cols': 80, 'rows': 30})}
        fields = ('title', 'text', 'category', 'tags', 'image')
        labels = {
            'title': 'Заголовок',
            'category': 'Раздел',
            'tags': 'Теги',
            'text': 'Текст',
            'image': 'Изображение',
        }
        help_texts = {
            'title': 'Введите заголовок',
            'category': 'Укажите раздел',
            'tags': 'Перечислите теги, к которым можно отнести пост',
            'text': 'Заполните текст',
            'image': 'Загрузите изображение (необязательно)',
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name', 'slug', 'text_color', 'background_color')
        labels = {
            'name': 'Название',
            'slug': 'Slug',
            'text_color': 'Цвет текста',
            'background_color': 'Цвет фона',
        }
        help_texts = {
            'name': 'Введите название',
            'slug': 'Slug (латиницей)',
            'text_color': 'Укажите HEX',
            'background_color': 'Укажите HEX',
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        labels = {
            'name': 'Название',
            'slug': 'Slug',
        }
        help_texts = {
            'name': 'Введите название',
            'slug': 'Slug (латиницей)',
        }
