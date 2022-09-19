from django.http import HttpResponse

from http.client import HTTPResponse
from pickletools import read_uint1
from urllib import request
from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.contrib.auth.models import User


CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)

def get_recipe(filter_recipe = None):
    if filter_recipe:
        print("DATA COMING FROM DB")
        
        recipes = Recipe.objects.filter(name__contains = filter_recipe)
    else:
        recipes = Recipe.objects.all()
    return recipes


def home(request):
    
    filter_recipe = request.GET.get('recipe')
    if cache.get(filter_recipe):
        print("DATA COMING FROM CACHE")
        recipe = cache.get(filter_recipe)
    else:
        if filter_recipe:
            recipe = get_recipe(filter_recipe)
            cache.set(filter_recipe, recipe)
        else:
            recipe = get_recipe()
        
    context = {'recipe': recipe}
    return render(request, 'home.html' , context)

def show(request , id):
    if cache.get(id):
        print("DATA COMING FROM CACHE")
        recipe = cache.get(id)
    else:
        print("DATA COMING FROM DB")

        recipe = Recipe.objects.get(id = id)
        cache.set(id , recipe)
    context = {'recipe' : recipe}
    return render(request, 'show.html' , context)

def order(request, id):
    user = request.user
    recipe = Recipe.objects.get(id=id)
    print(recipe)
    if recipe:
        if Order.objects.filter(recipe=recipe):
            return HttpResponse("order already")
    
    order = Order.objects.create(user=user, recipe=recipe)
    return HttpResponse("order successfull go to the my orders")

def user_orders(request):
    user = request.user
    user_orders = Order.objects.filter(user=user)
    print(user_orders)
    context = {
        'user_orders':user_orders
    }
    return render(request, 'user_orders.html', context )

def cart(request, id):
    user = request.user
    recipe = Recipe.objects.get(id=id)
    print(Cart.objects.all())
    
    
    if Cart.objects.filter(recipe=recipe):
        cart_update = Cart.objects.get(recipe=recipe)
        cart_update.quantity = cart_update.quantity+1
        cart_update.total = cart_update.quantity * cart_update.recipe.price
        cart_update.save()
        cart = Cart.objects.all()
        return render(request, 'cart.html', {"cart":cart})
    else:   
        Cart(user=user, recipe=recipe).save()
        cart = Cart.objects.all()
        return render(request, 'cart.html', {"cart":cart} )
    
    
   