# Generated by Django 5.0.7 on 2024-07-28 06:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_learning_app', '0002_pdf_pdf_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='quiz',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
