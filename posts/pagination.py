from rest_framework.pagination import PageNumberPagination



class MyPageNumberPagination(PageNumberPagination):
    page_query_param='page'