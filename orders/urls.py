from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reserve/', views.reserve_table, name='reserve_table'),
    path('place_order/', views.place_order, name='place_order'),
    path('menu/', views.menu, name='menu'),
]
