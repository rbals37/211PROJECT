from django import forms
from signup.models import CustomUser


class UserEditForm(forms.ModelForm):
    current_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': '현재 비밀번호'}),
        label="현재 비밀번호"
    )

    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': '새 비밀번호'}),
        label = "새 비밀번호"
    )

    class Meta:
        model = CustomUser
        fields = ['name', 'phone_number', 'user_id']  

    def clean_password(self):
        return self.instance.password

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 필드가 빈 값이어도 허용
        for field in self.fields.values():
            field.required = False
    