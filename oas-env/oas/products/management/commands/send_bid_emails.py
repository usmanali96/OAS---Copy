from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from products.models import Product

class Command(BaseCommand):
    help = 'Send emails when bid end time has passed'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        products = Product.objects.filter(bid_end_time__lte=now, bid_end_time__isnull=False)

        for product in products:
            if product.bids:
                highest_bid = max(product.bids, key=lambda bid: bid['price'])
                email = highest_bid.get('email')
                
                if email:
                    send_mail(
                        subject=f'Bid Winner for {product.title}',
                        message=f'Congratulations! You have the highest bid of {highest_bid["price"]} for {product.title}. Congrats for winning the Auction we will share the payment details soon.',
                        from_email='onlineauction537@gmail.com',
                        recipient_list=[email],
                    )
                    
                product.save()

        self.stdout.write(self.style.SUCCESS('Successfully sent bid end emails.'))