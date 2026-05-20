from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.main, name='main'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
]