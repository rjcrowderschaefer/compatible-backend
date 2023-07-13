from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name', 'category_description', 'category_img1', 'category_img2', 'category_img3', 'active_offer_total', 'created_at')