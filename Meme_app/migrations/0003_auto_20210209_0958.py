# Generated by Django 3.0.3 on 2021-02-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meme_app', '0002_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='URL',
            field=models.URLField(default='http://www.google.com'),
        ),
    ]
