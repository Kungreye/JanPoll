#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from django.urls import path

from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),                                # ex: /polls/
    path('<int:question_id>/', views.detail, name='detail'),            # ex: /polls/6/
    path('<int:question_id>/results/', views.results, name='results'),  # ex: /polls/6/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),           # ex: /polls/6/vote/
]
