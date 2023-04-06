import random

from django.core.management.base import BaseCommand
from currency.models import Rate, Source
from currency.choices import RateCurrencyChoices


class Command(BaseCommand):
    # help = "Generate random test rates"

    def handle(self, *args, **options):
        source, _ = Source.objects.get_or_create(code_name='privatbank', defaults={'name': 'PrivatBank'})

        for _ in range(10):
            Rate.objects.create(
                buy=random.randint(30, 40),
                sale=random.randint(30, 40),
                currency=random.choices(RateCurrencyChoices.choices)[0][0],
                source=source
            )


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         import string
#         from currency.models import ContactUs
#         for _ in range(10):
#             letters = string.ascii_lowercase
#             ContactUs.objects.create(
#                 name=''.join(random.choices(letters, k=10)),
#                 subject=''.join(random.choices(letters, k=10)),
#                 email=''.join(random.choices(letters, k=10)) + '@' + ''.join(random.choices(letters, k=10)) + '.com',
#                 message=''.join(random.choices(letters, k=100)),
#             )
