#!/usr/bin/env python 
# encoding: utf-8 
# author: jeremyZ
# time: 2020/7/7 1:26 下午
from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'pageSize'
    max_page_size = 20

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
            ('current_page', self.page.number),
            ('maximum_page', self.page.paginator.num_pages),
            ('page_size', self.get_page_size(self.request)),
        ]))
