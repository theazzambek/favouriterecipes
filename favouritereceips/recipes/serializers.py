from rest_framework import serializers
from .models import Category, Image, Recipes, Nutritions, Ingredients, Instructions, CookingTime, PreparationTime, Likes

class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ["image", "name", "user", "likes_recipes"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutritions
        fields = "__all__"

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        # fields = "__all__"
        exclude = ["id"]

class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructions
        # fields = "__all__"
        exclude = ["id"]

class CookingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingTime
        # fields = "__all__"
        exclude = ["id"]

class PreparationTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreparationTime
        # fields = "__all__"
        exclude = ["id"]

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        # fields = "__all__"
        exclude = ["id"]

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        # fields = "__all__"
        exclude = ["id"]


class RecipeDetailSerializer(serializers.ModelSerializer):
    image_recipes = ImageSerializer(many=True)
    nutrition_recipes = NutritionSerializer(many=True)
    ingredient_recipes = IngredientsSerializer(many=True)
    instructions_recipes = InstructionSerializer(many=True)
    cookingtime_recipes = CookingTimeSerializer(many=True)
    preparationtime_recipes = PreparationTimeSerializer(many=True)
    likes_recipes = LikesSerializer(many=True)

    class Meta:
        model = Recipes
        fields = ["user", 'name', "image_recipes", "nutrition_recipes", "description", "ingredient_recipes", "instructions_recipes", "serving", "cookingtime_recipes", "preparationtime_recipes", "likes_recipes", "categories",]