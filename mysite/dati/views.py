from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Result
from django.http import JsonResponse

# Create your views here.

def index(request):
    q = Question.objects.all()
    content = {
        'question_list':q
    }
    return render(request,'dati/dati.html',content)

def Get_score(request):
    data = {
        'name':'william'
    }
    if request.method == "GET":
        ans_list = request.GET.getlist('ans[]')
        time     = request.GET['time']
        #print(ans_list.getlist('ans[]')[2])
        ans_list = ans_list[1:]
        q = Question.objects.all()
        sum = 0
        for i in range(0,4):
            if ans_list[i] == q[i].answer:
                sum += 25
        data['score'] = sum
        r = Result(user='15001',score=sum,time=time)
        r.save()

    return JsonResponse(data)