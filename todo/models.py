from django.db import models
from django.urls import reverse


class Todo(models.Model):
    name = models.CharField("Название", max_length=128)
    description = models.TextField("Описание")
    complete_before = models.DateTimeField("Закончить до", blank=True, null=True)
    is_completed = models.BooleanField("Завершено", default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("todo_detail", args=[self.pk])

    class Meta:
        ordering = ("created_at", "name")
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
