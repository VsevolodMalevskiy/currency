from django.urls import path

from currency.views import (
    RateListView,
    RateCreateView,
    RateDetailView,
    RateUpdateView,
    RateDeleteView,
    RateTableView,
    SourceListView,
    SourceCreateView,
    SourceTableView,
    SourceDetailView,
    SourceUpdateView,
    SourceDeleteView,
    ContactUsListView,
    ContactUsCreateView,
    ContactUsTableView,
    ContactUsDetailView,
    ContactUsUpdateView,
    ContactUsDeleteView,
    RequestResponseLogListView,
    RequestResponseLogTableView,
)

app_name = 'currency'

urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/table/', RateTableView.as_view(), name='rate-table'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/table/', SourceTableView.as_view(), name='source-table'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
    path('contactus/list/', ContactUsListView.as_view(), name='contactus-list'),
    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus-create'),
    path('contactus/table/', ContactUsTableView.as_view(), name='contactus-table'),
    path('contactus/details/<int:pk>/', ContactUsDetailView.as_view(), name='contactus-details'),
    path('contactus/update/<int:pk>/', ContactUsUpdateView.as_view(), name='contactus-update'),
    path('contactus/delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contactus-delete'),
    path('log/table/', RequestResponseLogListView.as_view(), name='log-list'),
    path('log/list/', RequestResponseLogTableView.as_view(), name='log-table'),
]
