from django.db import models
from django.contrib.auth.models import User

from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('hot_drink', 'Hot Drink'),
        ('cold_drink', 'Cold Drink'),
        ('ice_cream', 'Ice Cream'),
        ('cake', 'Cake'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image_url = models.ImageField(upload_to='menu_items/')

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.PositiveIntegerField(default=1)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)  
    reservation_date = models.DateField()  
    reservation_time = models.TimeField()
    number_of_people = models.IntegerField()
    
    def __str__(self):
        return f"رزرو برای {self.fullname} در تاریخ {self.reservation_date} ساعت {self.reservation_time} برای {self.number_of_people} نفر"


