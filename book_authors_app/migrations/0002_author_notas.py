# Generated by Django 3.2.5 on 2021-08-11 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notas',
            field=models.CharField(default='null', max_length=250),
            preserve_default=False,
        ),
    ]