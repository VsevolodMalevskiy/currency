from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    EUR = 1, 'Euro'
    USD = 2, 'Dollar'
    CHF = 3, 'SuiFrank'
    PLN = 4, 'Zloty '
    GBP = 5, 'Pound'
