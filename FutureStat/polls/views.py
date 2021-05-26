from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latsest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    return HttpResponse(template.render(context, request))
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
# Create your views here.


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

