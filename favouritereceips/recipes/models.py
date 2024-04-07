from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.admin import User


class Category(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.title


class Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField()
    serving = models.SmallIntegerField(default=0)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Nutritions(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="nutrition_recipes")
    calories = models.SmallIntegerField(default=0)
    carbohydrates = models.SmallIntegerField(default=0)
    squirrel = models.SmallIntegerField(default=0)
    sodium = models.SmallIntegerField(default=0)
    net_carb = models.SmallIntegerField(default=0)
    fat = models.SmallIntegerField(default=0)


class Ingredients(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="ingredient_recipes")
    text = models.TextField()

    def __str__(self):
        return self.text


class Instructions(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="instructions_recipes")
    text = models.TextField()

    def __str__(self):
        return self.text

class CookingTime(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="cookingtime_recipes")
    hour = models.SmallIntegerField(default=0)
    minute = models.SmallIntegerField(default=0)


class PreparationTime(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="preparationtime_recipes")
    hour = models.SmallIntegerField(default=0)
    minute = models.SmallIntegerField(default=0)


class Likes(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="likes_recipes")
    likes = models.BooleanField(default=False)


class Image(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name='Рецепты', related_name="image_recipes")
    image = models.ImageField(upload_to='recipe_photo/', verbose_name='Фото')

    def __str__(self):
        return f"{self.recipes} - {self.image}"