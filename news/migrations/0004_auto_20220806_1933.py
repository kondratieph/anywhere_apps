# Generated by Django 3.2.13 on 2022-08-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20220730_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]