from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from currency.models import Rate, ContactUs
from currency.forms import RateForm


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
    global form
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'form': form
    }
    return render(request, 'rates_create.html', context)


def rates_update(request, pk):
    rate = get_object_or_404(Rate, pk=pk)  # проверка на наличие id, если нет, ошибка 404

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)  # Instance=rate не добавляет, а перезаписывает по id объект
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        # try:
        #     rate = Rate.objects.get(id=pk)
        # except Rate.DoesNotExist:
        #     raise Http404('Rate does not exist')

        form = RateForm(instance=rate)

        context = {
            'form': form
        }
        return render(request, 'rates_update.html', context)


def rates_delete(request, pk):
    rate = get_object_or_404(Rate, pk=pk)  # проверка на наличие id, если нет, ошибка 404
    if request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        context = {
        'rate': rate
        }
        return render(request, 'rates_delete.html', context)


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


@csrf_exempt
def request_methods(request):
    '''
    1. GET - client wants to get data from server (read)
    http:\\localhost:8000\path\?name=John&age=27
    2. POST - client wants push data to server (create)
    http:\\localhost:8000\path\
    name=John&age=27
    3. PUT - client wants update record on server (update) name=John&age=28
    4. PATCH - client wants update record on server partially (partial update) name=John or age=27
    5. DELETE - client wants to delete record on server (delete)
    6. OPTIONS - client wants to know which methods are available
    7. HEAD (GET) - client wants info about (without body)
    HTML - GET, POST
    C - POST
    R - GET (list, details)
    U - PUT\PATCH
    D - DELETE
    '''
    global message
    if request.method == 'GET':
        message = 'GET method'
    elif request.method == 'POST':
        message = 'POST method'
    return HttpResponse(message)
