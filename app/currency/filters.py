import django_filters

from currency.models import Rate, ContactUs, Source, RequestResponseLog


class RateFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = ['buy', 'sale']


class RateAPIFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = {
            'buy': ('gt', 'gte', 'lt', 'lte', 'exact'),  # подключение операторов для поиска: >,=>,<,=<,=
            'sale': ('gt', 'gte', 'lt', 'lte', 'exact'),
        }


class ContactUsFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = ['name', ]


class ContactusAPIFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = {
            'name': ('iendswith', 'istartswith', 'iexact', 'icontains'),
            'subject': ('iendswith', 'istartswith', 'iexact', 'icontains'),
        }


class SourceFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        fields = ['name', ]


class SourceAPIFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        fields = {
            'name': ('iendswith', 'istartswith', 'iexact', 'icontains'),
            'code_name': ('iendswith', 'istartswith', 'iexact', 'icontains'),
        }


class RequestResponseLogFilter(django_filters.FilterSet):

    class Meta:
        model = RequestResponseLog
        fields = ['request_method', ]
