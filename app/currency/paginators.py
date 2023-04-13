from rest_framework.pagination import PageNumberPagination


class RatesPagination(PageNumberPagination):
    page_size = 10                      # стандартный размер страницы
    page_size_query_param = 'page_size'
    max_page_size = 100                 # допустимое значение возможных изменений клиентом лично строк на странице


class SourcesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ContactusesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class RequestResponseLogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
