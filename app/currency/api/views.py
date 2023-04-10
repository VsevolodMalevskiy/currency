# from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer


from currency.api.serializers import RateSerializer
from currency.models import Rate


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

    # создание формы под запрос (не обязательно прописывать - для примера функция).
    # detail=True - создает путь /api/currency/rates/<pk>/buy/.принимает только метод POST по данному запросу.
    # возвращает тип валюты currency и стоимость buy в переменной rate (закомиченный print)
    @action(detail=True, methods=('POST',))
    def buy(self, request, *args, **kwargs):
        rate = self.get_object()
        # print(rate)  # send buy request
        sz = self.get_serializer(instance=rate)
        return Response(sz.data)
