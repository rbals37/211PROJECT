from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserEditForm 
from signup.models import CustomUser
from django.contrib.auth import update_session_auth_hash

def mypage(request):
    return render(request,'mypage.html')

def edit_mypage(request):
    user = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            for field, value in form.cleaned_data.copy().items():
                if field in ['current_password', 'new_password']:
                    continue
                if value != getattr(user, field):
                    setattr(user, field, value)     

            current_password = form.cleaned_data.get('current_password')
            new_password = form.cleaned_data.get('new_password')
            
            if current_password and new_password:
                    if not user.check_password(current_password):
                        form.add_error('current_password', "현재 비밀번호가 올바르지 않습니다.")
                        messages.error(request, '잘못된 입력값 입니다.')
                        return render(request, 'edit_mypage.html', {'form': form})
                    else:
                        user.set_password(new_password)  # 비밀번호 해싱
                        update_session_auth_hash(request, user)  # 세션 유지

            user.save()
            return redirect('mypage')
        
        else:
            messages.error(request, '잘못된 입력값 입니다.')            
    else:
         form = UserEditForm(instance=user)

    return render(request, 'edit_mypage.html', {'form': form})