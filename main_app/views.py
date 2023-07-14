from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, FeedbackSerializer
from .models import Category, Feedback

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class FeedbackView(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()