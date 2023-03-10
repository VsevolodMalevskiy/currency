from django.contrib import admin
from currency.models import Rate, ContactUs, Source, RequestResponseLog


@admin.register(ContactUs)
class ContactusAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'name',
        'email',
        'subject',
        'message'
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'source_url',
        'name',
        'phone'
    )


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'buy',
        'sell',
        'currency',
        'source',
        'created',
    )


@admin.register(RequestResponseLog)
class RequestResponseLogAdmin(admin.ModelAdmin):
    list_display = (
        'path',
        'request_method',
        'time'
    )
