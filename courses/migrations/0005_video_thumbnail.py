# Generated by Django 5.1.2 on 2025-03-11 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_payment_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='video_thumbnails/'),
        ),
    ]
