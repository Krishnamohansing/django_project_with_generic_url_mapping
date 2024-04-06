from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(request):
    return HttpResponse('Mr. Captain Cool')
def virat(request):
    return HttpResponse('<h1>King kohli</h1>')
def rohit(request):
    return HttpResponse('<h1><marquee>one of the greatest opner</marquee></h1>')
