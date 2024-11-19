from django import forms
from .models import CustomUser


class CustomSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['name', 'phone_number', 'birth_date', 'user_id', 'password']  # 이름, 전화번호, 생년월일, 아이디, 비밀번호


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # 비밀번호 해시
        if commit:
            user.save()
        return user