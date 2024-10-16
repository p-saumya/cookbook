# Generated by Django 5.1.1 on 2024-09-21 05:05

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('name', models.CharField(max_length=300)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('img', models.ImageField(upload_to='')),
                ('category', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.recipe')),
            ],
        ),
    ]
