# coding=utf-8
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 400

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'meta': {
                'pages': self.page.paginator.num_pages,
                'count': self.page.paginator.count,
            },
            'results': data
        })
