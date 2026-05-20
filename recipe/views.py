from django.shortcuts import render
from .models import Recipe 

def main(request):
    recipes = Recipe.objects.filter(created_at__year=2023)
    return render(request, 'recipe/main.html', {'recipes': recipes})