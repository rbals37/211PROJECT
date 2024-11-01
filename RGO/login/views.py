from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from signup.models import CustomUser



def login_view(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(student_id=student_id)
        except CustomUser.DoesNotExist:
            messages.error(request, '잘못된 학번입니다.')
            return redirect('login')
        
        
        user = authenticate(request, student_id=student_id, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('main')
        else:
            messages.error(request, '잘못된 비밀번호입니다.')
    
    
    return render(request, "login.html")

def logout_view(request):
    auth_logout(request)
    return redirect('main') 