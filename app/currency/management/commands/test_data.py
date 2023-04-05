import random

from django.core.management.base import BaseCommand, CommandError
from currency.models import Rate, Source
from currency.choices import RateCurrencyChoices


class Command(BaseCommand):
    help = "Generate random test rates"

    def handle(self, *args, **options):
        source, _ = Source.objects.get_or_create(code_name='privatbank', defaults={'name': 'PrivatBank'})

        for _ in range(100):
            Rate.objects.create(
                buy=random.randint(30, 40),
                sale=random.randint(30, 40),
                currency=random.choices(RateCurrencyChoices.choices)[0][0],
                source=source
            )
