from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=50)
    desc = models.TextField()
    image = models.CharField(max_length=400)

    def __str__(self):
        return self.name    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe')
    
    def __str__(self):
        return f"{self.user} & {self.recipe.name}"   

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cart')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='cart_recipe')
    total = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    sub_total = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user} & {self.recipe.name}"  
    
    

