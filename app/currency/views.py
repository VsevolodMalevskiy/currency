# from django.shortcuts import render
from django.http import HttpResponse

from currency.models import Rate, ContactUs


def list_rates(request):
    qs = Rate.objects.all()
    result = []
    for rate in qs:
        result.append(f'id: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, currency: {rate.currency}, '
                      f'source: {rate.source}, created: {rate.created} <br>')
    return HttpResponse(str(result))


def list_contact_us(request):
    qs = ContactUs.objects.all()
    result = []
    for contact_us in qs:
        result.append(f'id: {contact_us.id}, email_from: {contact_us.email_from}, subject: {contact_us.subject}, '
                      f'message: {contact_us.message}, <br>')
    return HttpResponse(str(result))
