from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class ToDo(models.Model):
    title = models.CharField(max_length=80, verbose_name = 'Задача')
    status = models.BooleanField(default=False, verbose_name = 'Выполнено / Не выполнено')
    due_date = models.DateField(null=True, blank=True, verbose_name = 'Дата выполнения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        # ordering = ['-pk']

