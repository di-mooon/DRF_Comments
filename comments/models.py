from django.db import models


class Articles(models.Model):
    """Статья"""
    title = models.CharField('Название статьи', max_length=250)
    author = models.CharField('Автор', max_length=250)
    text = models.TextField('Текст')
    is_published = models.BooleanField('Публикация', default=True)
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'


class Comments(models.Model):
    """Комментарий к статье"""
    name = models.CharField('Имя пользователя', max_length=250)
    text = models.TextField('Текст')
    date = models.DateField('Дата', auto_now_add=True)
    is_published = models.BooleanField('Публикация', default=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name='Родитель',
        related_name='children'
    )
    articles = models.ForeignKey(
        Articles,
        on_delete=models.CASCADE,
        verbose_name='Статья',
        related_name="comments"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
