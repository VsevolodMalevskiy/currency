from django.core.cache import cache
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from currency.filters import RateAPIFilter, SourceAPIFilter, ContactusAPIFilter, RequestResponseLogFilter

from currency.api.serializers import RateSerializer, SourceSerializer, ContactusSerializer, RequestResponseLogSerializer
from currency.models import Rate, Source, ContactUs, RequestResponseLog

from currency.paginators import RatesPagination, SourcesPagination, ContactusesPagination, RequestResponseLogPagination
from currency.throttlers import AnonCurrencyThrottle

from currency.choices import RateCurrencyChoices
from currency import constants


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = SourcesPagination
    permission_classes = (AllowAny,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    filterset_class = SourceAPIFilter
    ordering_fields = ('name', 'code_name')
    search_fields = ['id', 'name', 'code_name']


class ContactusViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactusSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = ContactusesPagination
    permission_classes = (AllowAny,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    filterset_class = ContactusAPIFilter
    ordering_fields = ('id', 'created', 'name', 'subject', 'email')
    search_fields = ['id', 'created', 'name', 'subject', 'email']


class RequestResponseLogApiView(generics.ListAPIView):
    queryset = RequestResponseLog.objects.all()
    serializer_class = RequestResponseLogSerializer
    permission_classes = (AllowAny,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    filterset_class = RequestResponseLogFilter
    ordering_fields = ('id', 'request_method')
    search_fields = ['id', 'request_method']
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = RequestResponseLogPagination


# class RateApiView(generics.ListCreateAPIView):  # ListCreateAPIView включает в себя create,list
#     queryset = Rate.objects.all().select_related('source')
#     serializer_class = RateSerializer  # под капотом делает json.dumps, json.loads
#
#
# class RateDetailApiView(generics.RetrieveUpdateDestroyAPIView):  # RetrieveUpdateDestroyAPIView: delete,detail,update
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer


#  оптимизированный класс для create, list, details, delete, update, но необходимо вместо path прописать router в urls
class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    # закомитил для проверки def latest кэширование
    # renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)  # в каком формате передача данных: json,xml,yaml
    pagination_class = RatesPagination  # пагинация из класса RatesPagination в фале paginators.py

    # параметр AllowAny прописывается, если класс должен отличаться от параметров установленных в setting.py.
    # В данном случае для этого класса не будет требоваться токен
    permission_classes = (AllowAny,)
    filter_backends = (                         # подключение фильтров из существующих
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,  # подключение библиотеки для сортировки
        rest_framework_filters.SearchFilter,    # подключение библиотеки для search
    )
    filterset_class = RateAPIFilter
    ordering_fields = ('id', 'created', 'buy', 'sale', 'source')  # поля, по каким при желании возможна сортировка
    search_fields = ['id', 'created', 'buy', 'sale', 'source__name']  # поля для search
    throttle_classes = (AnonCurrencyThrottle,)  # ограничение по количеству запросов в период времени

    # создание формы под запрос (не обязательно прописывать - для примера функция).
    # detail=True - создает путь /api/currency/rates/<pk>/buy/.принимает только метод POST по данному запросу.
    # возвращает тип валюты currency и стоимость buy в переменной rate (закомиченный print)
    @action(detail=True, methods=('POST',))
    def buy(self, request, *args, **kwargs):
        rate = self.get_object()
        # print(rate)  # send buy request
        sz = self.get_serializer(instance=rate)
        return Response(sz.data)

    # для кеширования повторных запросов
    # !!!вызов http://127.0.0.1:8000/api/currency/rates/latest/
    @action(detail=False, methods=('GET',))
    def latest(self, request, *args, **kwargs):
        latest_rates = []
        # key = 'API::currency::rates::latest'  # перенесено в constants.py
        # вызов как constants.LATEST_RATE_CACHE для визуализации, что это именно константа
        cached_rates = cache.get(constants.LATEST_RATE_CACHE)

        # удаление кэша при обновлении БД организовано в сигналах в файле receivers.py
        # для работы кэширования необходимо запустить файл memcached.exe на диске
        if cached_rates:
            return Response(cached_rates)

        for source_obj in Source.objects.all():
            for currency in RateCurrencyChoices:
                latest = Rate.objects.filter(source=source_obj, currency=currency).order_by('-created').first()
                if latest:
                    latest_rates.append(RateSerializer(instance=latest).data)

        cache.set(constants.LATEST_RATE_CACHE, latest_rates, 60 * 60 * 24)  # сутки
        return Response(latest_rates)
