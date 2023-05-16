from django.contrib import admin
from .models import FoodCategory, Food, WasteCategory, FoodWaste

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'amount' ,'description')

@admin.register(WasteCategory)
class WasteCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(FoodWaste)
class FoodWasteAdmin(admin.ModelAdmin):
    list_display = ('food', 'category', 'amount', 'date_recorded')
