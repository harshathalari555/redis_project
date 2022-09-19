from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [

    path('',home , name='home'),
    path('<int:id>',show , name='show'),
    path('order/<int:id>/',order , name='order'),
    path('user-orders/',user_orders , name='user-orders'),
    path('cart/<int:id>/',cart , name='cart'),
    
]
