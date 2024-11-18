from django.shortcuts import render

# Create your views here.

def mypage(quest):
    return render(quest,'mypage.html')