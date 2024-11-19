from django.shortcuts import render

# Create your views here.

def mypage(quest):
    return render(quest,'mypage.html')

def edit_mypage(quest):
    return render(quest, 'edit_mypage.html')

