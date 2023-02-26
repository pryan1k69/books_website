from homepage.models import Books
from django.forms import ModelForm, TextInput, Textarea

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'text', 'img', 'author_fn', 'author_ln']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название книги'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое содержание'
            }),
            'author_fn': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя автора'
            }),
            'author_ln': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия автора'
            }),
        }