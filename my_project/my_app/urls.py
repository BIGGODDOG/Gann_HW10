from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('add/', views.add_restaurant, name='add_restaurant'),
    path('delete/<int:restaurant_id>/', views.delete_restaurant, name='delete_restaurant'),
    path('edit/<int:restaurant_id>/', views.edit_restaurant, name='edit_restaurant'),
    path('search/', views.search_restaurant, name='search_restaurant'),

]
