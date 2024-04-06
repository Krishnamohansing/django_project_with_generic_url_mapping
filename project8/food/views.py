from django.shortcuts import render

# Create your views here.
def biryani(request):
    return render(request,'biryani.html')
def chicken(request):
    return render(request,'chicken.html')
