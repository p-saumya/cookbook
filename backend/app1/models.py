from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200,unique=True)
    category = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.recipe.name}"