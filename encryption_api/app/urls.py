from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('encode/', EncodeView.as_view()),
    #path('decode/')
]
