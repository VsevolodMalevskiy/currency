# from django.urls import path
# from currency.api.views import RateApiView, RateDetailApiView

from currency.api.views import RateViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api-currency'

router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rates')  # basename='rates' - задает path('rates/'

urlpatterns = [
    # path('rates/', RateApiView.as_view(), name='rates-list'),
    # path('rates/<int:pk>/', RateDetailApiView.as_view(), name='rates-details')
]

urlpatterns += router.urls
