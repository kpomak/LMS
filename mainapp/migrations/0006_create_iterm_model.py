# Generated by Django 3.2.15 on 2022-10-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0005_data_teachers"),
    ]

    operations = [
        migrations.CreateModel(
            name="Interim_news",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("body", models.TextField(blank=True, null=True, verbose_name="Interim_body")),
            ],
        ),
    ]
