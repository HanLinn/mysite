from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@login_required
def results(request, question_id):
    response = "You're at the results of question %s."
    return HttpResponse(response % question_id)


@login_required
def vote(request, question_id):
    return HttpResponse("You're voting quesition %s." % question_id)
