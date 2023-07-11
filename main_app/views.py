from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TestClassSerializer
from .models import TestClass

# Create your views here.

class TestView(viewsets.ModelViewSet):
    serializer_class = TestClassSerializer
    queryset = TestClass.objects.all()
