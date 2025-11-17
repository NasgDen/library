from django.db import models

class News(models.Model):
    """ Описание полей модели - Новости """
    title = models.CharField(max_length=150, verbose_name="Название новости", help_text="Введите название новости")
    content = models.TextField(verbose_name="Содержание новости", help_text="Введите содержание новости")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_ut = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
