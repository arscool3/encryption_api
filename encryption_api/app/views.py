from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
# Create your views here.
from .models import *
from .serializers import *

class EncodeView(generics.CreateAPIView) :
    permission_classes = (AllowAny, )
    queryset = Encoder.objects.all()
    serializer_class = EncoderCreateSerializer
