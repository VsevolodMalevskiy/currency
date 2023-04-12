from rest_framework.throttling import AnonRateThrottle


class AnonCurrencyThrottle(AnonRateThrottle):
    scope = 'currency'       # количество запросов указано в 'DEFAULT_THROTTLE_RATES' в settngs.py
