# Generated by Django 4.2.2 on 2023-06-10 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='svg',
            field=models.FileField(blank=True, upload_to='images'),
        ),
    ]
