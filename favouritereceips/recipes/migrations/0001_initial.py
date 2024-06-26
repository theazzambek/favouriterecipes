# Generated by Django 5.0.3 on 2024-04-07 05:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField()),
                ('serving', models.SmallIntegerField(default=0)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreparationTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.SmallIntegerField(default=0)),
                ('minute', models.SmallIntegerField(default=0)),
                ('recipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preparationtime_recipes', to='recipes.recipes')),
            ],
        ),
        migrations.CreateModel(
            name='Nutritions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.SmallIntegerField(default=0)),
                ('carbohydrates', models.SmallIntegerField(default=0)),
                ('squirrel', models.SmallIntegerField(default=0)),
                ('sodium', models.SmallIntegerField(default=0)),
                ('net_carb', models.SmallIntegerField(default=0)),
                ('fat', models.SmallIntegerField(default=0)),
                ('recipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutrition_recipes', to='recipes.recipes')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.BooleanField(default=False)),
                ('recipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_recipes', to='recipes.recipes')),
            ],
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('recipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructions_recipes', to='recipes.recipes')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('recipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_recipes', to='recipes.recipes')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='recipe_photo/', verbose_name='Фото')),
                ('recipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_recipes', to='recipes.recipes', verbose_name='Рецепты')),
            ],
        ),
        migrations.CreateModel(
            name='CookingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.SmallIntegerField(default=0)),
                ('minute', models.SmallIntegerField(default=0)),
                ('recipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cookingtime_recipes', to='recipes.recipes')),
            ],
        ),
    ]
