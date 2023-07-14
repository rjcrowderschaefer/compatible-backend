from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, ListingSerializer, FeedbackSerializer
from .models import Category, Listing, Feedback

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ListingView(viewsets.ModelViewSet):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

class FeedbackView(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()