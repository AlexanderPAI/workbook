from django import forms

from articles.models import Article


class ArticleForm(forms.ModelForm):
    """Форма создания/редактирования поста."""
    class Meta:
        model = Article
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