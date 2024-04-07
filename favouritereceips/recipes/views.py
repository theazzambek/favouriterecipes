from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ViewSet
from .models import *
from .serializers import *


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class NutritionView(generics.ListAPIView):
    queryset = Nutritions.objects.all()
    serializer_class = NutritionSerializer
    permission_classes = [AllowAny]

class IngredientsView(generics.ListAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [AllowAny]

class InstructionView(generics.ListAPIView):
    queryset = Instructions.objects.all()
    serializer_class = InstructionSerializer
    permission_classes = [AllowAny]

class CookingTimeView(generics.ListAPIView):
    queryset = CookingTime.objects.all()
    serializer_class = CookingTimeSerializer
    permission_classes = [AllowAny]

class PreparationTimeView(generics.ListAPIView):
    queryset = PreparationTime.objects.all()
    serializer_class = PreparationTimeSerializer
    permission_classes = [AllowAny]

class LikesView(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [AllowAny]


class RecipesListView(generics.ListAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeListSerializer
    permission_classes = [AllowAny]

class RecipesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeDetailSerializer
    permission_classes = [AllowAny]