from django.shortcuts import render

# Create your views here.
def assignment(request):
    return render(request,'assignment1.HTML')
def htmlform(request):
    return render(request,'html form2.html')

