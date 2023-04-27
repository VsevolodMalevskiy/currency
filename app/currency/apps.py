from django.apps import AppConfig


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'

    def ready(self):
        import currency.receivers
        # добавил для исключения сработки flake8 из-за неявного вызова import currency.receivers
        # как и в account/apps.py
        currency.receivers.Rate
