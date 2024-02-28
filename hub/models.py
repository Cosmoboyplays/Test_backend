from django.db import models


class Products(models.Model):
    author = models.CharField(max_length=150, unique=True, verbose_name='Автор')
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    created_timestamp = models.DateTimeField(verbose_name='Дата старта')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')

    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name}'


class Lessons(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_link = models.URLField()

    class Meta:
        db_table = 'lesson'
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ("id",)

    def __str__(self):
        return f'{self.title}'


class Groups(models.Model):
