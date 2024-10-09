from django.urls import path
from . import views

urlpatterns = [
    path('getRecipes/', views.get_recipes, name='get_recipes'),
    path('getRecipeDetails/<str:pk>/', views.get_recipe_details, name='get_recipe_details'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('likeRecipe/<str:pk>/', views.like_recipe, name='like_recipe'),
    path('addComment/<str:pk>/', views.add_comment, name='add_comment'),
    path('recipes/search/', views.search_recipes, name='search_recipes'),
    path('delete_recipe/<str:recipe_name>/', views.delete_recipe, name='delete_recipe'),
]