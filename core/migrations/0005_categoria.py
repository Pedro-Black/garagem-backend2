# Generated by Django 5.0.6 on 2024-07-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_rename_acessorio_acessorio_descricao_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
    ]
