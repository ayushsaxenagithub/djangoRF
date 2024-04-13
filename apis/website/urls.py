from django.contrib import admin
from django.urls import path,include
from .views import PersonList, profilecrud,DetailsList, DetailsCrud, FullDetails

urlpatterns = [
    path('',PersonList,name = 'person_list'),
    path('person/<int:pk>/',profilecrud,name = 'person_curd'),
    path('details/',DetailsList.as_view(),name = 'details_list'),
    path('details/<int:pk>/',DetailsCrud.as_view(),name ='detailcrud'),
    path('profile/<int:pk>/',FullDetails.as_view(),name ='fulldetails'),
]
