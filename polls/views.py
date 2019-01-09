#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello. We are now at the polls index.")
