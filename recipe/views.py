from django.shortcuts import render
from .models import Recipe 

def main(request):
    recipes = Recipe.objects.filter(created_at__year=2023)
    return render(request, 'recipe/main.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})    