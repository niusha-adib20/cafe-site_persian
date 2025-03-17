from django.shortcuts import render , redirect
from .models import Order, Reservation, MenuItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user)
    reservations = Reservation.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {'orders': orders, 'reservations': reservations})

@login_required
def reserve_table(request):
    if request.method == 'POST':
        fullname = request.POST.get('name')
        reservation_date = request.POST.get('date')
        reservation_time = request.POST.get('time')
        number_of_people = request.POST.get('people')

        reservation = Reservation.objects.create(
            user=request.user,
            fullname=fullname,
            reservation_date=reservation_date,
            reservation_time=reservation_time,
            number_of_people=number_of_people
        )

        messages.success(request, '!رزرو شما با موفقیت ثبت شد')

        return redirect('reservation')

    return render(request, 'reservation.html')

@login_required
def place_order(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        quantity = request.POST.get('quantity')

        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("تعداد باید یک عدد مثبت باشد.")
        except (ValueError, TypeError):
            messages.error(request, "تعداد وارد شده صحیح نیست.")
            return redirect('menu')

        try:
            menu_item = MenuItem.objects.get(name=item_name)
            price = menu_item.price
        except MenuItem.DoesNotExist:
            messages.error(request, "آیتم پیدا نشد.")
            return redirect('menu')

        total_price = price * quantity
        
        last_order = Order.objects.filter(user=request.user).count()
        new_order_number = last_order + 1

        Order.objects.create(
            user=request.user,
            order_number=new_order_number,
            item_name=item_name,
            quantity=quantity,
            price=total_price,
        )

        messages.success(request, "!سفارش شما با موفقیت ثبت شد")
        return redirect('menu')

    return redirect('menu')

def menu(request):
    
    hot_drinks = MenuItem.objects.filter(category='hot_drink')
    cold_drinks = MenuItem.objects.filter(category='cold_drink')
    ice_creams = MenuItem.objects.filter(category='ice_cream')
    cakes = MenuItem.objects.filter(category='cake')

    
    return render(request, 'menu.html', {
        'hot_drinks': hot_drinks,
        'cold_drinks': cold_drinks,
        'ice_creams': ice_creams,
        'cakes': cakes,
    })


