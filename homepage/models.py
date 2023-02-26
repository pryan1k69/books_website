from django.db import models
from django.contrib.auth.models import User



class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название книги', max_length=255)
    text = models.TextField(verbose_name='Краткое содержание')
    created_on = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    img = models.ImageField(verbose_name='Фото', upload_to='books/image/', default='books/image/default.png')
    author_fn = models.CharField(verbose_name='Имя автора', max_length=255, default='Без имени')
    author_ln = models.CharField(verbose_name='Фамилия автора', max_length=255, default='Без фамилии')

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'
        ordering = ('created_on',)

    def __str__(self):
        return '{} создана @{}'.format(self.name, self.user.username)

    def get_absolute_url(self):
        return f'/book/{self.id}'





