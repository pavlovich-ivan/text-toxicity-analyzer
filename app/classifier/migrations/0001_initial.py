# Generated by Django 4.2.2 on 2023-07-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Results",
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
                ("comment_text", models.TextField()),
                ("toxic", models.BooleanField()),
                ("severe_toxic", models.BooleanField()),
                ("obscene", models.BooleanField()),
                ("threat", models.BooleanField()),
                ("insult", models.BooleanField()),
                ("identity_hate", models.BooleanField()),
            ],
        ),
    ]
