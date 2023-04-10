import django_filters

from currency.models import Rate, ContactUs, Source, RequestResponseLog


class RateFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = ['buy', 'sale']


class ContactUsFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = ['name', ]


class SourceFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        fields = ['name', ]


class RequestResponseLogFilter(django_filters.FilterSet):

    class Meta:
        model = RequestResponseLog
        fields = ['request_method', ]