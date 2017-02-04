from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:6]
    context = {'latest_question_list' : latest_question_list,}
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question':question,})

def results(request, question_id):
    response = "You'r looking at the response of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You'r voting on the question %s" % question_id)
