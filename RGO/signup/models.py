from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, name, phone_number,birth_date, user_id ,  password=None):
        if not user_id:
            raise ValueError('아이디 입력 필요')
        if not birth_date:
            raise ValueError('생년월일 입력 필요')
        user = self.model(name=name, phone_number =phone_number, birth_date =birth_date , user_id = user_id)
        user.set_password(password)  # 비밀번호 해시화
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=4) 
    user_id = models.CharField(max_length=15, unique=True) 
    phone_number = models.CharField(max_length = 11)
    birth_date = models.DateField(default='2000-01-01')

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.user_id