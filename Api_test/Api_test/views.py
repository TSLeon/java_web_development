from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Welcome to Api_text index.")
    return render(request,'apis/Home.html')
