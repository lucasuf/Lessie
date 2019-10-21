from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    #return HttpResponse("This is the page for radio log interpretation")
    return render(request, 'base.html')


def upload(request):
    return render(request, 'upload.html')