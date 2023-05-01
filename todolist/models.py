from django.db import models


class ToDo(models.Model):
    title = models.CharField('Название задания', max_length=50, help_text='Название задания')
    is_complete = models.BooleanField("Завершено", default=False, help_text='Название задания')
    #user = models.CharField('name', max_length=50)

    class Meta:
        verbose_name = "Задания"
        verbose_name_plural = "Задания"

    def __str__(self):
        return self.title
