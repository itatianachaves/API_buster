# Generated by Django 4.2.6 on 2023-10-10 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(default=None, null=True),
        ),
    ]