from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def krishna(request):
    return HttpResponse("<center><h1>krishna is a good Studend</h1></center>")
def htmlform(request):
    return render(request,'htmlform.html')