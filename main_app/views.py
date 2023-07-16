from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, ListingSerializer, FeaturedListingSerializer, FeedbackSerializer
from .models import Category, Listing, Feedback, FeaturedListing

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ListingView(viewsets.ModelViewSet):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

class FeaturedListingView(viewsets.ModelViewSet):
    serializer_class = FeaturedListingSerializer
    queryset = FeaturedListing.objects.all()

class FeedbackView(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()