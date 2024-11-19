from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserEditForm 
from signup.models import CustomUser
import time


def mypage(quest):
    return render(quest,'mypage.html')

def edit_mypage(request):
    user = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            for field, value in form.cleaned_data.items():
                if value != getattr(user, field):
                    setattr(user, field, value)            
            return redirect('mypage')
        
        else:
            messages.error(request, '잘못된 입력값 입니다.')            
    else:
         form = UserEditForm(instance=user)

    return render(request, 'edit_mypage.html', {'form': form})