# Generated by Django 5.0.6 on 2024-07-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_acessorio_options_alter_cor_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="marca",
            name="nacionalidade",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
