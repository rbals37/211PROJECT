from django import forms
from signup.models import CustomUser


class UserEditForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['name', 'phone_number', 'birth_date', 'user_id']  

    def clean_password(self):
        return self.instance.password

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 필드가 빈 값이어도 허용
        for field in self.fields.values():
            field.required = False
    