#!/usr/bin/env python 
# encoding: utf-8 
# author: jeremyZ
# time: 2020/7/7 2:39 下午
from rest_framework.filters import BaseFilterBackend

from charts.apis.serializer import ClientChartsModel


class ChartsFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return ClientChartsModel.objects.all().order_by('created_at').distinct('user')