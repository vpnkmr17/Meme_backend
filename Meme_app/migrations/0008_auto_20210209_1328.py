# Generated by Django 3.0.3 on 2021-02-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meme_app', '0007_auto_20210209_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='URL',
            field=models.URLField(max_length=1000),
        ),
    ]