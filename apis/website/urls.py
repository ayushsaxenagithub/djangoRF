from django.contrib import admin
from django.urls import path,include
from .views import PersonList, profilecrud

urlpatterns = [
    path('',PersonList,name = 'person_list'),
    path('person/<int:pk>',profilecrud,name = 'person_curd')
]
