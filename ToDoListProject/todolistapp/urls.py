from django.contrib import admin
from django.urls import path
from todolistapp import views


urlpatterns = [
    path("",views.login, name="login"),
    path("home",views.index,name="home"),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('task/',views.task, name='task')



]
