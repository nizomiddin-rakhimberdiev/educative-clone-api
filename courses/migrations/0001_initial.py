# Generated by Django 4.0.4 on 2022-05-04 19:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('duration', models.CharField(max_length=50)),
                ('number_of_students', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('target', models.CharField(max_length=200)),
                ('course_picture', models.ImageField(upload_to='')),
                ('to_whom', models.CharField(max_length=100)),
                ('introduction_video', models.URLField(default='https://www.youtube.com/')),
            ],
            options={
                'ordering': ['last_update'],
            },
        ),
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('profile_picture', models.ImageField(upload_to='')),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('stars_given', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('count_rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
