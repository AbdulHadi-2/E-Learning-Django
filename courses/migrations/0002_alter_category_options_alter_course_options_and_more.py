# Generated by Django 5.1.2 on 2024-11-28 20:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='mentor',
            options={'verbose_name_plural': 'Mentors'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_url',
        ),
        migrations.AddField(
            model_name='course',
            name='introduction_video',
            field=models.FileField(blank=True, null=True, upload_to='course_introductions/'),
        ),
        migrations.AddField(
            model_name='payment',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='stripe_payment_intent',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(default='1.mp4', upload_to='course_videos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('user', 'course')},
        ),
    ]
