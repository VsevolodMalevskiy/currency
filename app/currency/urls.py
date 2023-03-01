from django.urls import path

from currency.views import (
    RateListView,
    RateCreateView,
    RateDetailView,
    RateUpdateView,
    RateDeleteView,
    RateTableView
)

app_name = 'currency'


urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/table/', RateTableView.as_view(), name='rate-table'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
]
