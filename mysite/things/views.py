from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the things index.")

def create(request):
    return HttpResponse("create thing")

def list(request):
    return HttpResponse("list of things")

def update(request, question_id):
    return HttpResponse("update %s." % question_id)

def delete(request, question_id):
    return HttpResponse("delete %s." % question_id)