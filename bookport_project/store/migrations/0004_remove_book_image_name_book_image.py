# Generated by Django 4.1.2 on 2023-06-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image_name',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
