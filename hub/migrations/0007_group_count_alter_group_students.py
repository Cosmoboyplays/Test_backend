# Generated by Django 4.2.8 on 2024-03-01 11:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hub', '0006_alter_group_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='count',
            field=models.PositiveIntegerField(default=0, verbose_name='Пользователей в группе'),
        ),
        migrations.AlterField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='group_set', to=settings.AUTH_USER_MODEL, verbose_name='Студенты'),
        ),
    ]