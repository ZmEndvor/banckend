#!/usr/bin/env python 
# encoding: utf-8 
# author: jeremyZ
# time: 2020/7/7 1:06 下午
from charts.models import ClientChartsModel
from rest_framework.serializers import Serializer


class ClientChartsSerializer(Serializer):
    class Meta:
        model = ClientChartsModel
        fields = '__all__'