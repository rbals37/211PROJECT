from django import forms
from .models import CustomUser

class CustomSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['student_id', 'name', 'password']  # 학번, 이름, 비밀번호만 받음

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # 비밀번호 해시
        if commit:
            user.save()
        return user