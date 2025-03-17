from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),  
    path('login/', views.user_login, name='login'),
    path('signUp/', views.register, name='register'), 
    path('reservation/', views.reservation, name='reservation'),
    path('logout/', views.user_logout, name='logout'),
]
