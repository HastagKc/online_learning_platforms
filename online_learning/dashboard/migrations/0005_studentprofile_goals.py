# Generated by Django 5.0.6 on 2024-07-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_studentprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='goals',
            field=models.CharField(default='', max_length=200),
        ),
    ]
