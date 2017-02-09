from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:6]
    context = {'latest_question_list' : latest_question_list,}
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/details.html', {'question':question,})

def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render (request, 'polls/details.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.post['choice'])
    except (KeyError, Choice.DoesNotExist)
        # redisplay the question
        return render(request, 'polls/details.html', {'question':question,'error_message':"You diddn't selected a choice"})
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect('polls:results', args = (question.id),)
