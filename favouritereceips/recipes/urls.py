from django.urls import path, include
from .views import *

urlpatterns = [
    path("category/", CategoryView.as_view()),
    path("category/<int:pk>/", CategoryView.as_view()),
    path("recipes/", RecipesListView.as_view()),
    path("recipes/<int:pk>/", RecipesDetailView.as_view()),
    path("nutrition/", NutritionView.as_view()),
    path("ingredients/", IngredientsView.as_view()),
    path("instructions/", InstructionView.as_view()),
    path("cookingtime/", CookingTimeView.as_view()),
    path("preparationtime/", PreparationTimeView.as_view()),
    path("likes/", LikesView.as_view()),
]