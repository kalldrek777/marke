from django.contrib import admin
from django.urls import path
from weapons.views import *
from weapons.views import knife, weapons, wear, stickers, accessories

urlpatterns = [
    path('knifes/', knife, name='knife_page'),
    path('weapons/', weapons, name='weap_page'),
    path('wear/', wear, name='wear'),
    path('stickers/', stickers, name='stickers'),
    path('accessories/', accessories, name='accessories'),
]