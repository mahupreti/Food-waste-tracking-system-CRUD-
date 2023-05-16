from django import forms
from .models import FoodCategory, Food, WasteCategory, FoodWaste 
# from django.forms.widgets import DateInput

class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = ['name']

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'category', 'amount', 'description']

class WasteCategoryForm(forms.ModelForm):
    class Meta:
        model = WasteCategory
        fields = ['name']

class FoodWasteForm(forms.ModelForm):
    class Meta:
        model = FoodWaste
        fields = ['food', 'category', 'amount']
        # widgets = {
        #     'date_recorded': DateInput(attrs={'type': 'date'}),
        # }
