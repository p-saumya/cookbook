from rest_framework import serializers
from .models import Recipe, Step, Ingredient, Comment

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['name']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at']

class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'img', 'category', 'likes', 'steps', 'ingredients', 'comments']