import os

from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
# Create your views here.
from django.http import HttpResponse, Http404, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods

from polls.models import Question
from django.views import generic


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    # raise Http404('just for test 404')
    return JsonResponse({'mes': output}, safe=True)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    # 获取对象获取不到返回404 官方提供的函数更简洁
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    with transaction.atomic():
        transaction.on_commit()
    s1 = transaction.savepoint()
    transaction.savepoint_commit(s1)
    transaction.rollback()
    return HttpResponse("You're voting on question %s." % question_id)


# 多文件上传
@require_http_methods(["GET", "POST"])
@csrf_exempt
def file(request):
    myfiles = request.FILES.getlist('myfile', None)
    for myfile in myfiles:
        path = os.path.join('.', myfile.name)
        with open(path, 'wb') as f:
            for chunk in myfile.chunks():
                f.write(chunk)
    return HttpResponse('upload success!')


def to_index(request):
    return redirect(reverse('polls:index'))
