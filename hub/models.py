from django.db import models

from users.models import User


class Products(models.Model):
    author = models.CharField(max_length=150, unique=True, verbose_name='Автор')
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    created_timestamp = models.DateTimeField(verbose_name='Дата старта')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    min_users = models.PositiveIntegerField(default=0, verbose_name='Минимальное количество студентов')
    max_users = models.PositiveIntegerField(default=10, verbose_name='Максимальное количество студентов')

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


class Group(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=150, verbose_name='Название группы')
    students = models.ManyToManyField(User, related_name='group_set', blank=True, verbose_name='Ученики')

    class Meta:
        db_table = 'group'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name}'
