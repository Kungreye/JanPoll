#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from django.urls import path

from . import views


app_name = 'polls'

# `generic.DetailView` expects the primary key value captured from the URL to be called "pk",
# so `question_id` is changed to `pk`.
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),                          # ex: /polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),               # ex: /polls/6/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),     # ex: /polls/6/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),                   # ex: /polls/6/vote/
]
