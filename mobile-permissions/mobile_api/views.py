from mobile_api.models import MobileModel
from typing import Generic
from django.shortcuts import render
from rest_framework import generics
from .serializer import MobileSerializer

# Create your views here.

class MobileView(generics.ListCreateAPIView):
    serializer_class= MobileSerializer
    queryset= MobileModel.objects.all()

class MobileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= MobileSerializer
    queryset= MobileModel.objects.all()