from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm, ContactUsForm

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView


class RateListView(ListView):
    template_name = 'rates_list.html'
    queryset = Rate.objects.all()


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rates_details.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rates_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UpdateView):
    form_class = RateForm
    template_name = 'rates_update.html'
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('currency:rate-list')


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


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    template_name = 'contactuses_create.html'
    success_url = reverse_lazy('currency:contactus-list')


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
