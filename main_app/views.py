from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, ContactSerializer
from .models import Category, Contact

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()