from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginpage),
    path('login.do', views.logindo),
    path('index', views.indexpage),
]