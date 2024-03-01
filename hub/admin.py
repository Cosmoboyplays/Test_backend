from django.contrib import admin

from .models import Products, Lessons, Group


class GroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('students',)  # Это позволит выбирать пользователей из списка для добавления в группу

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Добавляем пользователей в группу после сохранения
        obj.students.set(form.cleaned_data['students'])


admin.site.register(Group, GroupAdmin)
admin.site.register(Products)
admin.site.register(Lessons)
