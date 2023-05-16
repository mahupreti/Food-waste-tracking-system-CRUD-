from django.db import models

class FoodCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class WasteCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FoodWaste(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    category = models.ForeignKey(WasteCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_recorded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.food.name} - {self.amount} kg"

