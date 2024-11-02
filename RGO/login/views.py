from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from signup.models import CustomUser



def login_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(user_id=user_id)
        except CustomUser.DoesNotExist:
            messages.error(request, '잘못된 아이디입니다.')
            return redirect('login')
        
        
        user = authenticate(request, user_id=user_id, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('main')
        else:
            messages.error(request, '잘못된 비밀번호입니다.')
    
    
    return render(request, "login.html")

def logout_view(request):
    auth_logout(request)
    return redirect('main') 