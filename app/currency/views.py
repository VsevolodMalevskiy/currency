from currency.models import Rate, ContactUs, Source, RequestResponseLog
from currency.forms import RateForm, SourceForm, ContactUsForm, RegisterUserForm
from django.contrib.auth import get_user_model
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
        sender = 'User@gmail.com'
        recipient = 'support@rambler.ru'
        message = f'''
            Request from: {self.object.name}
            Reply to email: {self.object.email}
            Subject: {self.object.subject}
            Body: {self.object.message}
        '''

        from django.core.mail import send_mail
        send_mail(
            subject,
            message,
            sender,
            [recipient, sender],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class ProfileView(LoginRequiredMixin, UpdateView):        # mixin для исключения доступа к профайлу по прямой ссылке
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('index')
    model = get_user_model()                     # Возвращает модель пользователя, которая сейчас используется
    fields = (
        'first_name',
        'last_name'
    )

    # при регистрации нескольких админов исключает возможность редактирования чужого профиля
    def get_object(self, queryset=None):
        return self.request.user


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')
