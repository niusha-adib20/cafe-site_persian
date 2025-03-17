from django.contrib import admin
from .models import Order, Reservation
from .models import MenuItem

admin.site.register(Order)
admin.site.register(Reservation)
admin.site.register(MenuItem)
