from django.shortcuts import render

from django.http import HttpResponse
from .models import Thing


def index(request):
    latest_thing_list = Thing.objects.order_by('-pub_date')[:10]
    return render(request,'things/index.html')

def create(request):
    return HttpResponse("create thing")

def list(request):
    return HttpResponse("list of things")

def update(request, question_id):
    return HttpResponse("update %s." % question_id)

def delete(request, question_id):
    return HttpResponse("delete %s." % question_id)