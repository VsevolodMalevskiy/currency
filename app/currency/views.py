# from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render

from currency.models import Rate, ContactUs


# def list_rates(request):
#     qs = Rate.objects.all()
#     result = []
#     for rate in qs:
#         result.append(f'id: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, currency: {rate.currency}, '
#                       f'source: {rate.source}, created: {rate.created} <br>')
#     return HttpResponse(str(result))


# def list_contact_us(request):
#     qs = ContactUs.objects.all()
#     result = []
#     for contact_us in qs:
#         result.append(f'id: {contact_us.id}, email_from: {contact_us.email_from}, subject: {contact_us.subject}, '
#                       f'message: {contact_us.message}, <br>')
#     return HttpResponse(str(result))

def rates_create(request):

    context = {
    }
    return render(request, 'rates_create.html', context)


def list_rates(request):
    rates = Rate.objects.all()

    context = {
        'rates': rates
    }
    return render(request, 'rates_list.html', context)


def list_rates_7(request):
    rates = Rate.objects.all()

    context = {
        'rates': rates
    }
    return render(request, 'rates_list_7.html', context)


def list_contact_us(request):
    contactus = ContactUs.objects.all()

    context = {
        'contactus': contactus
    }
    return render(request, 'contactus_list.html', context)


