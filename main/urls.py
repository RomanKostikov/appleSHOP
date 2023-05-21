from django.urls import path, re_path
from django.contrib import admin
from main import views
urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    path('', views.index, name='start'),
]
