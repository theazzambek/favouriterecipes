from django.urls import path, include
from .views import *

urlpatterns = [
    path("category/", CategoryAPIView.as_view()),
    path("recipes/", RecipesListAPIView.as_view()),
    path("recipes/<int:pk>/", RecipesDetailAPIView.as_view()),
    path("nutrition/", NutritionAPIView.as_view()),
    path("ingredients/", IngredientsAPIView.as_view()),
    path("instructions/", InstructionAPIView.as_view()),
    path("cookingtime/", CookingTimeAPIView.as_view()),
    path("preparationtime/", PreparationTimeAPIView.as_view()),
    path("likes/", LikesAPIView.as_view()),
    path('send_email/', SendEmailView.as_view()),
]