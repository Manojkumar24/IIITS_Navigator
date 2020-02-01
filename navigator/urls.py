from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:floor_num>/', views.floor, name='floor'),
    path('<str:loc>', views.getEvent, name='getEvent'),
    path('eventLocationList/', views.eventLocationList, name='eventLocationList'),
    path('classesList/', views.classesList, name='classesList'),
    path('professorDetails/', views.professorDetails, name='professorDetails'),
]
