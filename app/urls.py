from django.contrib import admin
from django.urls import path 
from app.views import *

urlpatterns = [
    path('',home , name = 'home'),
    path('login' , login , name = 'login'),
    path('logout' , logout , name = 'logout'),
    path('register' , register , name = 'register'),
    path('add_todo' , add_todo , name = 'add_todo'),
    path('delete_todo/<int:id>' , delete_todo , name = 'delete_todo'),
    path('change_status/<int:id>/<str:status>' , change_status , name = 'change_status')

]
