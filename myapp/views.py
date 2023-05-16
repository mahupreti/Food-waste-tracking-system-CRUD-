from django.shortcuts import render, redirect
from .models import Food, FoodWaste
from .forms import FoodForm, FoodWasteForm


def home(request):
    return render(request, 'myapp/home.html')

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'myapp/food_list.html', {'foods': foods})

def food_create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm()
    return render(request, 'myapp/food_create.html', {'form': form})

def food_update(request, pk):
    food = Food.objects.get(pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm(instance=food)
    return render(request, 'myapp/food_update.html', {'form': form, 'food': food})

def food_detail(request, pk):
    food = Food.objects.get(pk=pk)
    return render(request, 'myapp/food_detail.html', {'food': food})

def foodwaste_list(request):
    foodwastes = FoodWaste.objects.all()
    return render(request, 'myapp/foodwaste_list.html', {'foodwastes': foodwastes})

def foodwaste_create(request):
    if request.method == 'POST':
        form = FoodWasteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foodwaste_list')
    else:
        form = FoodWasteForm()
    return render(request, 'myapp/foodwaste_create.html', {'form': form})

def foodwaste_update(request, pk):
    foodwaste = FoodWaste.objects.get(pk=pk)
    if request.method == 'POST':
        form = FoodWasteForm(request.POST, instance=foodwaste)
        if form.is_valid():
            form.save()
            return redirect('foodwaste_list')
    else:
        form = FoodWasteForm(instance=foodwaste)
    return render(request, 'myapp/foodwaste_update.html', {'form': form, 'foodwaste': foodwaste})

def foodwaste_detail(request, pk):
    foodwaste = FoodWaste.objects.get(pk=pk)
    return render(request, 'myapp/foodwaste_detail.html', {'foodwaste': foodwaste})

