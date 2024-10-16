# Generated by Django 5.1.1 on 2024-09-26 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0002_alter_ingredient_recipe_alter_step_recipe"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="ingredients_list",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="recipe",
            name="likes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="recipe",
            name="steps_list",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="recipe",
            name="category",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="img",
            field=models.ImageField(upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="name",
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="app1.recipe",
                    ),
                ),
            ],
        ),
    ]
