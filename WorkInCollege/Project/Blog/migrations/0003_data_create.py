# Generated by Django 4.1 on 2024-02-24 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_data_login_alter_data_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
