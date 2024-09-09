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
            for bid in product.bids:
                email = bid.get('email')
                if email:
                    send_mail(
                        subject=f'Bid Ended for {product.title}',
                        message=f'The bid for {product.title} has ended. Thank you for participating!',
                        from_email='onlineauction537@gmail.com',
                        recipient_list=[email],
                    )

            product.bids.clear()
            product.save()

        self.stdout.write(self.style.SUCCESS('Successfully sent bid end emails.'))