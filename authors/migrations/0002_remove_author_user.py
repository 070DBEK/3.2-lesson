# Generated by Django 5.1.5 on 2025-03-01 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
    ]
