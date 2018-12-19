from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import loader
from polls.models import Question, Choice
from django.utils import timezone
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect


def add_data(request):
    Question(question_text='什么是java', pub_date=timezone.now()).save()
    Question(question_text='什么是scala', pub_date=timezone.now()).save()
    Question(question_text='什么是python', pub_date=timezone.now()).save()
    return HttpResponse('success')


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')
    result = ','.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context=context)
    # return HttpResponse(template.render({}, request))


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('this question dose not exist')
    question = get_object_or_404(Question, pk=question_id)
    choice = get_list_or_404(Choice, question_id=question_id)
    return render(request, 'polls/detail.html', {"question": question, 'choices': choice})


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = get_list_or_404(Choice, question_id=question_id)
    return render(request, 'polls/results.html', {"question": question, 'choices': choices})


def vote(request, question_id):
    choice_id = request.POST['choice']
    choice = get_object_or_404(Choice, pk=choice_id)
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('polls:result', args=(choice.question_id,)))
