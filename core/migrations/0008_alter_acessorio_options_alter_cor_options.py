# Generated by Django 5.0.6 on 2024-07-12 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_marca"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="acessorio",
            options={"verbose_name": "Acessório", "verbose_name_plural": "Acessórios"},
        ),
        migrations.AlterModelOptions(
            name="cor",
            options={"verbose_name": "Cor", "verbose_name_plural": "Cores"},
        ),
    ]
