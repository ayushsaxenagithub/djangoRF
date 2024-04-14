from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('whoami/', WHOAMI.as_view(),name= 'whoami'),
    path('login/', LoginView.as_view(),name= 'login'),
    path('logout/',LogoutView.as_view(),name= 'logout'),
    path('register/',RegisterView.as_view(),name= 'register'),
]