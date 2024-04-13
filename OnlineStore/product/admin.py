from django.contrib import admin
from .models import Category, Item
# Register your models here.
@admin.register(Category)
class CategoryAmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Item)
class ItemAmin(admin.ModelAdmin):
    list_display = ['name', 'stock', 'sold', 'prize', 'category']