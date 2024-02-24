from django import forms

from tinymce.widgets import TinyMCE

from articles.models import Article


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