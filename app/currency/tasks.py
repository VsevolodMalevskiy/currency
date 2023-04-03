from celery import shared_task
from currency.choices import RateCurrencyChoices

from currency.constants import PRIVATBANK_CODE_NAME, MONOBANK_CODE_NAME, CREDITDNEPRBANK_CODE_NAME
from currency.utils import to_2_places_decimal

import requests
from bs4 import BeautifulSoup


@shared_task
def parse_creditdneprbank():
    from currency.models import Rate, Source

    source, _ = Source.objects.get_or_create(
        code_name=CREDITDNEPRBANK_CODE_NAME,
        defaults={
            'name': 'CreditdneprBank',
        }
    )

    url = "https://creditdnepr.com.ua/currency"
    response = requests.get(url)
    main_text = response.text
    soup = BeautifulSoup(main_text)
    available_usd = soup.find("table", {"class": "table-s1 tac sticky-enabled"}).find("tr", {"class": "even"}).text
    available_eur = soup.find("table", {"class": "table-s1 tac sticky-enabled"}).findAll("tr", {"class": "odd"})[1].text
    rates = (available_usd, available_eur)

    available_currency = {
        "USD": RateCurrencyChoices.USD,
        "EUR": RateCurrencyChoices.EUR,
    }

    for rate in rates:
        buy = to_2_places_decimal(rate[7:12])  # округление до 2 знаков после запятой для сравнения с данными в БД
        sale = to_2_places_decimal(rate[12:])
        currency = rate[:3]

        last_rate = Rate.objects.filter(
            currency=available_currency[currency],
            source=source
        ) \
            .order_by('-created') \
            .first()
        if not last_rate or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=available_currency[currency],
                source=source
            )


@shared_task
def parse_monobank():
    from currency.models import Rate, Source

    source, _ = Source.objects.get_or_create(
        code_name=MONOBANK_CODE_NAME,
        defaults={
            'name': 'MonoBank',
        }
    )

    url = "https://api.monobank.ua/bank/currency"
    response = requests.get(url)
    response.raise_for_status()  # проверяет успешный ли запрос, выдаст ошибку при коде 400 и выше
    rates = response.json()

    available_currency = {
        840: RateCurrencyChoices.USD,
        978: RateCurrencyChoices.EUR,
    }

    for rate in rates:
        # исключение курса USD к EUR: currencyCodeA=978 и currencyCodeB=840 (словарь 3)
        if rate['currencyCodeA'] not in available_currency or rate['currencyCodeB'] in available_currency:
            continue
        buy = to_2_places_decimal(rate['rateBuy'])  # округление до 2 знаков после запятой для сравнения с данными в БД
        sale = to_2_places_decimal(rate['rateSell'])
        currency = available_currency[rate['currencyCodeA']]

        last_rate = Rate.objects.filter(
            currency=available_currency[rate['currencyCodeA']],
            source=source
        ) \
            .order_by('-created') \
            .first()
        if not last_rate or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=currency,
                source=source
            )


@shared_task
def parse_privatbank():
    from currency.models import Rate, Source

    # source = Source.objects.filter(code_name=PRIVATBANK_CODE_NAME).first()
    # if source is None:
    #     source = Source.objects.create(code_name=PRIVATBANK_CODE_NAME, name='PrivatBank')
    # аналог
    source, _ = Source.objects.get_or_create(   # возвращает кортеж
        code_name=PRIVATBANK_CODE_NAME,
        defaults={
            'name': 'PrivatBank',
        }
    )

    url = "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11"
    response = requests.get(url)
    response.raise_for_status()  # проверяет успешный ли запрос, выдаст ошибку при коде 400 и выше
    rates = response.json()

    available_currency = {
        "USD": RateCurrencyChoices.USD,
        "EUR": RateCurrencyChoices.EUR,
    }

    for rate in rates:
        if rate['ccy'] not in available_currency:
            continue
        buy = to_2_places_decimal(rate['buy'])  # округление до двух знаков после запятой для сравнения с данными в БД
        sale = to_2_places_decimal(rate['sale'])
        currency = rate['ccy']

        last_rate = Rate.objects.filter(
            currency=available_currency[currency],
            source=source
        ) \
            .order_by('-created') \
            .first()
        if not last_rate or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=available_currency[currency],
                source=source
            )


# @shared_task(autoretry_for=(ConnectionError,),  # при ошибке повтор отправки
#              retry_kwargs={'max_retries': 5})
# def send_mail(subject, message):
#     raise ConnectionError
# '''
#  1 - 2 sec
#  2 - 4 sec
#  3 - 8 sec
#  4 - 16 sec
#  5 - error
#  '''
@shared_task
def send_mail(subject, message):
    recipient = 'support@rambler.ru'
    sender = 'User@gmail.com'
    from django.core.mail import send_mail
    from time import sleep
    sleep(10)
    send_mail(
        subject,
        message,
        sender,
        [recipient, sender],
        fail_silently=False,
    )
