from django.shortcuts import render

# Create your views here.

def myrecord(request):
    return render(request, 'myrecord.html')
