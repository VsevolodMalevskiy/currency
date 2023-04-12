# from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from currency.filters import RateAPIFilter

from currency.api.serializers import RateSerializer
from currency.models import Rate

from currency.paginators import RatesPagination
from currency.throttlers import AnonCurrencyThrottle


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
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)  # в каком формате передача данных: json,xml,yaml
    pagination_class = RatesPagination  # пагинация из класса RatesPagination в фале paginators.py

    # параметр AllowAny прописывается, если класс должен отличаться от параметров параметры прописывается, если класс
    # должен отличаться от параметров установленных в setting.pyю В данном случае для этого класса не будет требоваться
    # токен
    permission_classes = (AllowAny,)
    filter_backends = (                         # подключение фильтров из существующих
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,  # подключение библиотеки для сортировки
    )
    filterset_class = RateAPIFilter
    ordering_fields = ('id', 'created', 'buy', 'sale', 'source')  # поля, по каким при желании возможна сортировка
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
