from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, student_id, name, password=None):
        if not student_id:
            raise ValueError('학번 입력 필요')
        user = self.model(student_id=student_id, name=name)
        user.set_password(password)  # 비밀번호 해시화
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, name, password=None):
        user = self.create_user(student_id, name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    student_id = models.CharField(max_length=5, unique=True)  # 학번 (5자리)
    name = models.CharField(max_length=30)  # 사용자 이름

    objects = CustomUserManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.student_id