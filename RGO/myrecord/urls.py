from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view , name='myrecord'),
    path('<str:date>/', views.record_by_date, name='record_by_date')
]