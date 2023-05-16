
from django.urls import path


from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('food/', views.food_list, name='food_list'),
    path('food/create/', views.food_create, name='food_create'),
    path('food/update/<int:pk>/', views.food_update, name='food_update'),
    path('food/detail/<int:pk>/', views.food_detail, name='food_detail'),
    path('foodwaste/', views.foodwaste_list, name='foodwaste_list'),
    path('foodwaste/create/', views.foodwaste_create, name='foodwaste_create'),
    path('foodwaste/update/<int:pk>/', views.foodwaste_update, name='foodwaste_update'),
    path('foodwaste/detail/<int:pk>/', views.foodwaste_detail, name='foodwaste_detail'),
] 
