# Generated by Django 4.2.4 on 2023-08-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "complete_before",
                    models.DateTimeField(blank=True, verbose_name="Закончить до"),
                ),
                ("is_completed", models.BooleanField(verbose_name="Завершено")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Задача",
                "verbose_name_plural": "Задачи",
                "ordering": ("created_at", "name"),
            },
        ),
    ]