#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# request = <HttpRequest object>

"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context is a dict mapping template variable names to Python objects.
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""


# `generic.ListView` defaults to use a template called `<app name>/<model name>_list.html`
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # override automatically generated context variable `question_list`
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last 5 published questions."""
        return Question.objects.order_by('-pub_date')[:5]


# `generic.DetailView` defaults to use a template called `<app name>/<model name>_detail.html`
# In our case, the default is 'polls/question_detail.html'
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])    # id of selected choice, as a string
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Avoid race conditions using F()
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
