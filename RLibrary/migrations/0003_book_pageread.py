# Generated by Django 4.0.1 on 2022-05-20 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RLibrary', '0002_rename_books_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pageRead',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
