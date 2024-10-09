from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe, Ingredient, Step, Comment
from .serializers import RecipeSerializer, CommentSerializer

@api_view(['GET'])
def get_recipes(request):
    category = request.GET.get('category', '')
    if category:
        recipes = Recipe.objects.filter(category__iexact=category)
    else:
        recipes = Recipe.objects.all()
    serializers = RecipeSerializer(recipes, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def get_recipe_details(request,pk):
    recipe = get_object_or_404(Recipe, id=pk)
    serializers = RecipeSerializer(recipe)
    return Response(serializers.data)

@api_view(['POST'])
def create_recipe(request):
    serializers = RecipeSerializer(data=request.data)
    if serializers.is_valid():
        recipe = serializers.save()
        ingredients = request.data.getlist('ingredients') 
        for ingredient in ingredients:
            Ingredient.objects.create(recipe=recipe, name=ingredient)
        steps = request.data.getlist('steps')  
        for step in steps:
            Step.objects.create(recipe=recipe, name=step)
        return Response(serializers.data, status=201)
    return Response(serializers.errors, status=400)

@api_view(['POST'])
def like_recipe(request,pk):
    recipe = get_object_or_404(Recipe, id=pk)
    recipe.likes += 1
    recipe.save()
    return Response({'likes': recipe.likes})

@api_view(['POST'])
def add_comment(request,pk):
    recipe = get_object_or_404(Recipe, id=pk)
    serializers = CommentSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save(recipe=recipe)
        return Response(serializers.data, status=201)
    return Response(serializers.errors, status=400)
    
@api_view(['GET'])
def search_recipes(request):
    query = request.GET.get('q', '')
    recipes = Recipe.objects.filter(name__icontains=query)
    serializers = RecipeSerializer(recipes, many=True)
    return Response(serializers.data)

@api_view(['DELETE'])
def delete_recipe(request,recipe_name):
    recipe = get_object_or_404(Recipe,name__icontains=recipe_name)
    recipe.delete()
    return Response({'message': 'Recipe deleted successfully!'})

