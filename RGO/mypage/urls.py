from django.urls import path
from . import views

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('edit/', views.edit_mypage, name='edit'),
]