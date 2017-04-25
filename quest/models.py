from django.db import models


class Quest(models.Model):
    """
    Модель задачи, определяемая названием и текстовым описанием.
    """
    title = models.CharField(max_length=255, verbose_name="Название задачи")
    abstract = models.TextField(verbose_name="Описание задачи")
    sub_task = models.ForeignKey('quest.Quest', related_name="sub", null=True, blank=True, verbose_name="Подзадача к")

    def __str__(self):
        return self.title
