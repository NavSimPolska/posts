# Generated by Django 3.2.7 on 2021-09-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_posts_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author_id',
            field=models.IntegerField(),
        ),
    ]
