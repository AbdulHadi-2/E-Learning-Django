# Generated by Django 5.1.2 on 2024-11-25 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_mentor',
            new_name='is_staff',
        ),
    ]
