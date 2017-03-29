# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.TextField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('template_file', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='error_404_visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_time', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=25)),
                ('user_agent', models.TextField()),
                ('url_requested', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=500)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=25)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('tag', models.CharField(max_length=500)),
                ('main_image', models.CharField(max_length=200)),
                ('main_image_caption', models.CharField(max_length=400)),
                ('folder', models.CharField(max_length=200, unique=True)),
                ('style', models.CharField(choices=[('course', 'Course Work'), ('extra', 'Extra Work'), ('ongoing', 'R')], max_length=200)),
                ('alt_text', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
                ('display_rank', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=500)),
                ('conection', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=25)),
                ('content', models.TextField()),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]