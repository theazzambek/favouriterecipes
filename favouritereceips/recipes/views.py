from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ViewSet
from .models import *
from .serializers import *


class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class NutritionAPIView(generics.ListCreateAPIView):
    queryset = Nutritions.objects.all()
    serializer_class = NutritionSerializer
    permission_classes = [AllowAny]

class IngredientsAPIView(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [AllowAny]

class InstructionAPIView(generics.ListCreateAPIView):
    queryset = Instructions.objects.all()
    serializer_class = InstructionSerializer
    permission_classes = [AllowAny]

class CookingTimeAPIView(generics.DestroyAPIView):
    queryset = CookingTime.objects.all()
    serializer_class = CookingTimeSerializer
    permission_classes = [AllowAny]

class PreparationTimeAPIView(generics.ListCreateAPIView):
    queryset = PreparationTime.objects.all()
    serializer_class = PreparationTimeSerializer
    permission_classes = [AllowAny]

class LikesAPIView(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [AllowAny]


class RecipesListAPIView(generics.ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeDetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [AllowAny]
    search_fields = ["name"]

class RecipesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeDetailSerializer
    permission_classes = [AllowAny]


class SendEmailView(APIView):
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        recipient_list = request.data.get('recipient_list')

        send_mail(subject, message, 'bekazzam38@gmail.com', recipient_list)
        return Response({'message': 'Email sent successfully'})

