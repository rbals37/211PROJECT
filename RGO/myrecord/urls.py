from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view , name='myrecord'),
    path('record/<str:date>/', views.record_by_date, name='record_by_date'),
    path('write/', views.record_write, name = 'write'),
]