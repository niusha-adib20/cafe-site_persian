from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta

# تابع تعیین زمان پایان مزایده (24 ساعت بعد از شروع)
def get_auction_end_time():
    return now() + timedelta(hours=24)

class Auction(models.Model):
    name = models.CharField(max_length=255)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    start_date = models.DateTimeField(default=now) 
    end_date = models.DateTimeField(default=get_auction_end_time) 
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)


    def __str__(self):
        return self.name

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-amount']  # مرتب‌سازی پیشنهادها از بیشترین به کمترین مقدار

    def __str__(self):
        return f"{self.user.username} - {self.amount}"


