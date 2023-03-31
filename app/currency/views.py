from currency.models import Rate, ContactUs, Source, RequestResponseLog
from currency.forms import RateForm, SourceForm, ContactUsForm, RegisterUserForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView


class RateListView(ListView):
    template_name = 'rates_list.html'
    queryset = Rate.objects.all().select_related('source')  # join..("currency_rate"."source_id"="currency_source"."id")


class RateDetailView(LoginRequiredMixin, DetailView):
    queryset = Rate.objects.all()
    template_name = 'rates_details.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rates_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UserPassesTestMixin, UpdateView):
    form_class = RateForm
    template_name = 'rates_update.html'
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()

    def test_func(self, queryset=None):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self, queryset=None):
        return self.request.user.is_superuser


class RateTableView(ListView):
    template_name = 'rates_table.html'
    queryset = Rate.objects.all()


class SourceListView(ListView):
    template_name = 'sources_list.html'
    queryset = Source.objects.all()


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'sources_details.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'sources_create.html'
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    template_name = 'sources_update.html'
    success_url = reverse_lazy('currency:source-list')
    queryset = Source.objects.all()


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    template_name = 'sources_delete.html'
    success_url = reverse_lazy('currency:source-list')


class SourceTableView(ListView):
    template_name = 'sources_table.html'
    queryset = Source.objects.all()


class ContactUsListView(ListView):
    template_name = 'contactuses_list.html'
    queryset = ContactUs.objects.all()


class ContactUsDetailView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'contactuses_details.html'


class ContactUsUpdateView(UpdateView):
    form_class = ContactUsForm
    template_name = 'contactuses_update.html'
    success_url = reverse_lazy('currency:contactus-list')
    queryset = ContactUs.objects.all()


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'contactuses_delete.html'
    success_url = reverse_lazy('currency:contactus-list')


class ContactUsTableView(ListView):
    template_name = 'contactuses_table.html'
    queryset = ContactUs.objects.all()


class IndexView(TemplateView):
    template_name = 'index.html'


class RequestResponseLogListView(ListView):
    template_name = 'log_list.html'
    queryset = RequestResponseLog.objects.all()


class RequestResponseLogTableView(ListView):
    template_name = 'log_table.html'
    queryset = RequestResponseLog.objects.all()


# class ContactUsCreateView(CreateView):
#     form_class = ContactUsForm
#     template_name = 'contactuses_create.html'
#     success_url = reverse_lazy('currency:contactus-list')


class ContactUsCreateView(CreateView):
    template_name = 'contactuses_create.html'
    success_url = reverse_lazy('currency:contactus-list')
    model = ContactUs
    form_class = ContactUsForm
    # fields = (
    #     'name',
    #     'email',
    #     'subject',
    #     'message'
    # )

    def _send_mail(self):
        subject = 'User ContactUs'
        # sender = 'User@gmail.com'
        # recipient = 'support@rambler.ru'
        message = f'''
            Request from: {self.object.name}
            Reply to email: {self.object.email}
            Subject: {self.object.subject}
            Body: {self.object.message}
        '''
        from currency.tasks import send_mail
        send_mail.delay(subject, message)  # delay - передача worker
        # send_mail.apply_async(args=[subject, message]) # алтернатива верхему методу
        '''
        0 - 8.59 | 9.00 - 19.00 | 19.01 23.59
           9.00  |    send      | 9.00 next day
        '''
        #  алтернативный метод - отправка в указанное время
        # from datetime import datetime, timedelta
        # send_mail.apply_async(
        #     kwargs={'subject': subject, 'message': message},
        #     # countdown=20   #  альтернатива sleep(20)
        #     # eta=datetime(2023, 3, 28, 20, 49, 0)
        # )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')
