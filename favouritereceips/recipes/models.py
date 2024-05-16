from django.db import models
from django.contrib.auth.admin import User


class Category(models.Model):
    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name="Фото",
    )

    title = models.CharField(
        max_length=64,
        unique=True,
        verbose_name="Категория",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категория"


class Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    name = models.CharField(max_length=64, unique=True, verbose_name="Рецепт")
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Фото")
    description = models.TextField(verbose_name="Описание")
    serving = models.SmallIntegerField(default=0, verbose_name="Порция")
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_recept', verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рецепты"
        verbose_name_plural = "Рецепт"


class Nutritions(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="nutrition_recipes", verbose_name="Рецепт")
    calories = models.SmallIntegerField(default=0, verbose_name="Калория")
    carbohydrates = models.SmallIntegerField(default=0, verbose_name="Углевод")
    squirrel = models.SmallIntegerField(default=0, verbose_name="Белки")
    sodium = models.SmallIntegerField(default=0, verbose_name="Натрий")
    net_carb = models.SmallIntegerField(default=0, verbose_name="Чистые углеводы")
    fat = models.SmallIntegerField(default=0, verbose_name="Жир")

    class Meta:
        verbose_name = "Нутритации"
        verbose_name_plural = "Нутритация"


class Ingredients(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="ingredient_recipes", verbose_name="Рецепт")
    text = models.TextField(verbose_name="Ингредиенты")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Ингредиенты"
        verbose_name_plural = "Ингредиент"


class Instructions(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="instructions_recipes", verbose_name="Рецепт")
    text = models.TextField(verbose_name="Инструкции")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Инструкции"
        verbose_name_plural = "Инструкция"

class CookingTime(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="cookingtime_recipes", verbose_name="Рецепт")
    hour = models.SmallIntegerField(default=0, verbose_name="Час")
    minute = models.SmallIntegerField(default=0, verbose_name="Минута")

    class Meta:
        verbose_name = "Время готовить"
        verbose_name_plural = "Время готовить"


class PreparationTime(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="preparationtime_recipes", verbose_name="Рецепт")
    hour = models.SmallIntegerField(default=0, verbose_name="Час")
    minute = models.SmallIntegerField(default=0, verbose_name="Минута")

    class Meta:
        verbose_name = "Время подготовки"
        verbose_name_plural = "Время подготовки"


class Likes(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="likes_recipes", verbose_name="Рецепт")
    likes = models.BooleanField(default=False, verbose_name="Лайки")

    class Meta:
        verbose_name = "Лайки"
        verbose_name_plural = "Лайк"


class Image(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name='Рецепты', related_name="image_recipes")
    image = models.ImageField(upload_to='recipe_photo/', verbose_name='Фото')

    def __str__(self):
        return f"{self.recipes} - {self.image}"

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"