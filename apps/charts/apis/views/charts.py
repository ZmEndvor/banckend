#!/usr/bin/env python 
# encoding: utf-8 
# author: jeremyZ
# time: 2020/7/7 1:06 下午
import datetime
from django.contrib.auth.models import User
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError

from utils.paginations import DefaultPageNumberPagination
from charts.apis.serializer import ClientChartsModel, ClientChartsSerializer


class ChartsViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    pagination_class = [DefaultPageNumberPagination]
    filter_backends = [DjangoFilterBackend]

    def create(self, request, *args, **kwargs):
        """
            上传客户端号和分数
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        now = datetime.datetime.now()
        client = data.get('client', '')
        points = data.get('points', '')
        if not client or not points:
            raise ValidationError('参数不能为空')

        user = User.objects.get(id=request.user.id)
        params = {
            'created_at': now,
            'updated_at': now,
            'client': client,
            'points': points,
            'user': user
        }
        serializer = self.get_serializer(data=params)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        """
            排行榜分页列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = self.filter_queryset(self.get_queryset())

        user = User.objects.get(id=request.user.id)
        user_client_charts = ClientChartsModel.objects.filter(user=user).first()
        client_charts_dict = {client.client: client for client in queryset}
        own_serializer = ClientChartsSerializer(client_charts_dict[user_client_charts.client])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({'list': serializer.data, 'own': own_serializer.data})

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
