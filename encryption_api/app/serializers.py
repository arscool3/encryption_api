from rest_framework import serializers
from .models import *

class EncoderCreateSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Encoder
        fields = '__all__'