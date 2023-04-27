from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from currency import constants

from currency.models import Rate


# Для работы кэширования необходимо запустить фалй memcached.exe на диске
# для включения сигнала в файле currencu.__init__.py прописать default_app_config = 'currency.apps.CurrencyConfig'
# в файле apps.py прописать     def ready(self): import currency.receivers
@receiver(post_save, sender=Rate)
def rate_create_clear_cache(sender, instance, created, **kwargs):
    # Если объект создается, то кэш удаляется
    if created:
        cache.delete(constants.LATEST_RATE_CACHE)
