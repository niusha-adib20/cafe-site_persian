from django.shortcuts import render, get_object_or_404, redirect
from .models import Auction, Bid
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.utils.timezone import now

def auction_list(request):
    auctions = Auction.objects.all()
    
    auction_data = []
    for auction in auctions:
        time_remaining = auction.end_date - now()
        total_seconds = max(0, int(time_remaining.total_seconds()))  # جلوگیری از مقدار منفی

        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        auction_data.append({
            'auction': auction,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        })

    return render(request, "auction_list.html", {"auctions": auction_data})


def auction_detail(request, auction_id):
    auction = get_object_or_404(Auction, id=auction_id)
    bids = auction.bids.all().order_by("-amount")  # مرتب‌سازی پیشنهادها از بیشترین به کمترین

    # زمان جاری را با در نظر گرفتن منطقه زمانی محلی بگیرید
    current_time = timezone.localtime(timezone.now())

    # محاسبه زمان باقی‌مانده
    time_remaining = auction.end_date - current_time
    total_seconds = int(time_remaining.total_seconds())

    # اگر زمان منفی باشد، نشان‌دهنده این است که مزایده تمام شده
    auction_ended = total_seconds <= 0
    winner = None

    if auction_ended and bids.exists():
        winner = bids.first().user  # بالاترین پیشنهاددهنده برنده است

    hours, remainder = divmod(max(total_seconds, 0), 3600)
    minutes, seconds = divmod(remainder, 60)

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "برای ثبت پیشنهاد باید وارد شوید.")
            return redirect("login")

        bid_amount = request.POST.get("bid_amount")
        try:
            bid_amount = float(bid_amount)
        except ValueError:
            messages.error(request, "مبلغ پیشنهادی معتبر نیست.")
            return redirect("auction_detail", auction_id=auction.id)

        if bid_amount <= auction.starting_price:
            messages.error(request, "مبلغ پیشنهادی باید بیشتر از قیمت پایه باشد.")
            return redirect("auction_detail", auction_id=auction.id)

        highest_bid = bids.first()
        if highest_bid and bid_amount <= highest_bid.amount:
            messages.error(request, "مبلغ پیشنهادی باید بیشتر از بالاترین پیشنهاد فعلی باشد.")
            return redirect("auction_detail", auction_id=auction.id)

        Bid.objects.create(auction=auction, user=request.user, amount=bid_amount, timestamp=timezone.now())
        messages.success(request, "پیشنهاد شما با موفقیت ثبت شد!")
        return redirect("auction_detail", auction_id=auction.id)

    return render(request, "auction_detail.html", {
        "auction": auction,
        "bids": bids,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "auction_ended": auction_ended,
        "winner": winner
    })
