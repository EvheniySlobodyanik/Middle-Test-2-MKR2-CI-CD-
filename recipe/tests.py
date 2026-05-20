from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Recipe

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        # Створення тестових даних
        self.recipe_2023 = Recipe.objects.create(
            title="Салат 2023",
            description="Смачний салат",
            created_at=timezone.datetime(2023, 5, 15, tzinfo=timezone.utc)
        )
        self.recipe_2024 = Recipe.objects.create(
            title="Суп 2024",
            description="Гарячий суп",
            created_at=timezone.datetime(2024, 1, 1, tzinfo=timezone.utc)
        )

    def test_main_view_status_and_template(self):
        """Тест перевіряє статус відповіді, шаблон та фільтрацію за 2023 рік"""
        response = self.client.get(reverse('recipe:main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/main.html')
        # Має містити рецепт за 2023 рік
        self.assertContains(response, self.recipe_2023.title)
        # Не повинно містити рецепт за 2024 рік
        self.assertNotContains(response, self.recipe_2024.title)

    def test_recipe_detail_view_status_and_template(self):
        """Тест перевіряє детальну сторінку існуючого рецепту"""
        response = self.client.get(reverse('recipe:recipe_detail', args=[self.recipe_2023.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/recipe_detail.html')
        self.assertContains(response, self.recipe_2023.title)
        self.assertContains(response, self.recipe_2023.description)

    def test_recipe_detail_view_404(self):
        """Тест перевіряє повернення 404 для неіснуючого id"""
        response = self.client.get(reverse('recipe:recipe_detail', args=[999]))
        self.assertEqual(response.status_code, 404)