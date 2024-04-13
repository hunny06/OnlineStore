from django.shortcuts import render
from .models import Item, Category
# Create your views here.

def home(request):
    items = Item.objects.all()
    return render(request, 'base/home.html',{"items" : items})