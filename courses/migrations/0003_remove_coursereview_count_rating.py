# Generated by Django 4.0.4 on 2022-05-05 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursereview',
            name='count_rating',
        ),
    ]
