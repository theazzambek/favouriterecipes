from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Recipes)
admin.site.register(Image)
admin.site.register(CookingTime)
admin.site.register(PreparationTime)
admin.site.register(Likes)
admin.site.register(Ingredients)
admin.site.register(Instructions)
admin.site.register(Nutritions)